"""Self-contained QR code generator + round-trip decoder (no third-party modules).

python qr.py "<text>" <out.png> [scale] [border] [level]
python qr.py --selftest

Byte mode, error-correction levels L/M/Q/H, versions 1-9 (enough for any
registration URL), automatic version and mask selection per ISO/IEC 18004.
`--selftest` encodes a set of payloads, decodes the resulting module matrix
back with `decode()` and asserts the text matches, and also checks every
Reed-Solomon block evaluates to zero at its generator roots.
"""
import sys
import zlib

MODE_BYTE = 4

# EC_SPEC[version][level] = (ec_codewords_per_block, [(block_count, data_per_block), ...])
EC_SPEC = {
    1: {"L": (7, [(1, 19)]), "M": (10, [(1, 16)]), "Q": (13, [(1, 13)]), "H": (17, [(1, 9)])},
    2: {"L": (10, [(1, 34)]), "M": (16, [(1, 28)]), "Q": (22, [(1, 22)]), "H": (28, [(1, 16)])},
    3: {"L": (15, [(1, 55)]), "M": (26, [(1, 44)]), "Q": (18, [(2, 17)]), "H": (22, [(2, 13)])},
    4: {"L": (20, [(1, 80)]), "M": (18, [(2, 32)]), "Q": (26, [(2, 24)]), "H": (16, [(4, 9)])},
    5: {"L": (26, [(1, 108)]), "M": (24, [(2, 43)]), "Q": (18, [(2, 15), (2, 16)]), "H": (22, [(2, 11), (2, 12)])},
    6: {"L": (18, [(2, 68)]), "M": (16, [(4, 27)]), "Q": (24, [(4, 19)]), "H": (28, [(4, 15)])},
    7: {"L": (20, [(2, 78)]), "M": (18, [(4, 31)]), "Q": (18, [(2, 14), (4, 15)]), "H": (26, [(4, 13), (1, 14)])},
    8: {"L": (24, [(2, 97)]), "M": (22, [(2, 38), (2, 39)]), "Q": (22, [(4, 18), (2, 19)]), "H": (26, [(4, 14), (2, 15)])},
    9: {"L": (30, [(2, 116)]), "M": (22, [(3, 36), (2, 37)]), "Q": (20, [(4, 16), (4, 17)]), "H": (24, [(4, 12), (4, 13)])},
}
ALIGN = {1: [], 2: [6, 18], 3: [6, 22], 4: [6, 26], 5: [6, 30], 6: [6, 34],
         7: [6, 22, 38], 8: [6, 24, 42], 9: [6, 26, 46]}
FORMAT_EC = {"L": 1, "M": 0, "Q": 3, "H": 2}
EC_FROM_BITS = {v: k for k, v in FORMAT_EC.items()}


def size(version):
    return 17 + 4 * version


# ---------------------------------------------------------------- GF(256)
GF_EXP = [0] * 512
GF_LOG = [0] * 256
_x = 1
for _i in range(255):
    GF_EXP[_i] = _x
    GF_LOG[_x] = _i
    _x <<= 1
    if _x & 0x100:
        _x ^= 0x11D
for _i in range(255, 512):
    GF_EXP[_i] = GF_EXP[_i - 255]


def _mul(a, b):
    if a == 0 or b == 0:
        return 0
    return GF_EXP[GF_LOG[a] + GF_LOG[b]]


def rs_generator(n):
    poly = [1]
    for i in range(n):
        nxt = [0] * (len(poly) + 1)
        for j, c in enumerate(poly):
            nxt[j] ^= c
            nxt[j + 1] ^= _mul(c, GF_EXP[i])
        poly = nxt
    return poly


def rs_ec(data, n):
    gen = rs_generator(n)
    rem = list(data) + [0] * n
    for i in range(len(data)):
        f = rem[i]
        if f:
            for j, g in enumerate(gen):
                rem[i + j] ^= _mul(g, f)
    return rem[len(data):]


def _rs_ok(block, n):
    """Full codeword must evaluate to 0 at every generator root."""
    for i in range(n):
        acc = 0
        for c in block:
            acc = _mul(acc, GF_EXP[i]) ^ c
        if acc != 0:
            return False
    return True


# ---------------------------------------------------------------- bit helpers
def _bch(data, gen, genbits):
    rem = data << (genbits - 1)
    for i in range(rem.bit_length() - 1, genbits - 2, -1):
        if rem >> i & 1:
            rem ^= gen << (i - (genbits - 1))
    return (data << (genbits - 1)) | rem


def _format_bits(level, mask):
    return _bch((FORMAT_EC[level] << 3) | mask, 0x537, 11) ^ 0x5412


def _version_bits(version):
    return _bch(version, 0x1F25, 13)


def _mask(mask, r, c):
    if mask == 0:
        return (r + c) % 2 == 0
    if mask == 1:
        return r % 2 == 0
    if mask == 2:
        return c % 3 == 0
    if mask == 3:
        return (r + c) % 3 == 0
    if mask == 4:
        return (r // 2 + c // 3) % 2 == 0
    if mask == 5:
        return (r * c) % 2 + (r * c) % 3 == 0
    if mask == 6:
        return ((r * c) % 2 + (r * c) % 3) % 2 == 0
    return ((r + c) % 2 + (r * c) % 3) % 2 == 0


# ---------------------------------------------------------------- layout
def skeleton(version):
    """Function patterns + reserved map + the ordered data-cell positions.

    Shared by encode() and decode() so the two can never disagree.
    """
    n = size(version)
    grid = [[0] * n for _ in range(n)]
    res = [[False] * n for _ in range(n)]

    def setf(r, c, v):
        if 0 <= r < n and 0 <= c < n:
            grid[r][c] = v
            res[r][c] = True

    for (fr, fc) in ((0, 0), (0, n - 7), (n - 7, 0)):
        for r in range(-1, 8):
            for c in range(-1, 8):
                if 0 <= fr + r < n and 0 <= fc + c < n:
                    dark = (2 <= r <= 4 and 2 <= c <= 4) or (
                        (r in (0, 6) or c in (0, 6)) and 0 <= r <= 6 and 0 <= c <= 6)
                    setf(fr + r, fc + c, 1 if dark else 0)
    for i in range(8, n - 8):
        v = 1 if i % 2 == 0 else 0
        setf(6, i, v)
        setf(i, 6, v)
    centers = ALIGN[version]
    for r in centers:
        for c in centers:
            if (r < 9 and c < 9) or (r < 9 and c > n - 10) or (r > n - 10 and c < 9):
                continue
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    setf(r + dr, c + dc, 1 if max(abs(dr), abs(dc)) != 1 else 0)
    setf(n - 8, 8, 1)

    # reserve format areas
    for i in range(9):
        res[8][i] = True
        res[i][8] = True
    for i in range(8):
        res[8][n - 1 - i] = True
        res[n - 1 - i][8] = True
    if version >= 7:
        for i in range(18):
            r, c = i // 3, i % 3
            res[n - 11 + c][r] = True
            res[r][n - 11 + c] = True

    order = []
    col, upward = n - 1, True
    while col > 0:
        if col == 6:
            col -= 1
        rows = range(n - 1, -1, -1) if upward else range(n)
        for r in rows:
            for c in (col, col - 1):
                if not res[r][c]:
                    order.append((r, c))
        upward = not upward
        col -= 2
    return grid, res, order


def _write_format(grid, version, level, mask):
    n = size(version)
    fbits = _format_bits(level, mask)
    for i in range(0, 6):
        grid[8][i] = (fbits >> i) & 1
    grid[8][7] = (fbits >> 6) & 1
    grid[8][8] = (fbits >> 7) & 1
    grid[7][8] = (fbits >> 8) & 1
    for i in range(9, 15):
        grid[14 - i][8] = (fbits >> i) & 1
    for i in range(0, 8):
        grid[n - 1 - i][8] = (fbits >> i) & 1
    for i in range(8, 15):
        grid[8][n - 15 + i] = (fbits >> i) & 1
    grid[n - 8][8] = 1
    if version >= 7:
        vbits = _version_bits(version)
        for i in range(18):
            bit = (vbits >> i) & 1
            r, c = i // 3, i % 3
            grid[n - 11 + c][r] = bit
            grid[r][n - 11 + c] = bit


# ---------------------------------------------------------------- encoding
def encode_blocks(text, level="M", version=None):
    """Return (version, data_blocks, ec_blocks) with padding applied."""
    raw = text.encode("utf-8")
    if level not in EC_SPEC[1]:
        raise ValueError("level must be L/M/Q/H")
    if version is None:
        for v in sorted(EC_SPEC):
            total = sum(c * d for c, d in EC_SPEC[v][level][1])
            cc = 8 if v <= 9 else 16
            if 4 + cc + 8 * len(raw) <= total * 8:
                version = v
                break
        if version is None:
            raise ValueError(f"payload too long for versions 1-9 at level {level}: {len(raw)} bytes")
    ec_pb, groups = EC_SPEC[version][level]
    total_data = sum(c * d for c, d in groups)
    cc = 8 if version <= 9 else 16

    bits = []

    def put(val, n):
        for i in range(n - 1, -1, -1):
            bits.append((val >> i) & 1)

    put(MODE_BYTE, 4)
    put(len(raw), cc)
    for b in raw:
        put(b, 8)
    cap = total_data * 8
    put(0, min(4, cap - len(bits)))
    while len(bits) % 8:
        bits.append(0)
    i = 0
    while len(bits) < cap:
        put([0xEC, 0x11][i % 2], 8)
        i += 1
    data = [int("".join(map(str, bits[i:i + 8])), 2) for i in range(0, len(bits), 8)]

    blocks, ecs, pos = [], [], 0
    for count, dlen in groups:
        for _ in range(count):
            blk = data[pos:pos + dlen]
            pos += dlen
            blocks.append(blk)
            ecs.append(rs_ec(blk, ec_pb))
    return version, blocks, ecs


def encode(text, level="M", version=None):
    """Return (version, interleaved codeword stream)."""
    version, blocks, ecs = encode_blocks(text, level, version)
    ec_pb = EC_SPEC[version][level][0]
    max_d = max(len(b) for b in blocks)
    stream = []
    for i in range(max_d):
        for b in blocks:
            if i < len(b):
                stream.append(b[i])
    for i in range(ec_pb):
        for e in ecs:
            stream.append(e[i])
    return version, stream


def matrix(text, level="M", version=None):
    version, stream = encode(text, level, version)
    bits = [(cw >> i) & 1 for cw in stream for i in range(7, -1, -1)]
    best = None
    for mask in range(8):
        grid, res, order = skeleton(version)
        for (r, c), bit in zip(order, bits):
            grid[r][c] = bit ^ (1 if _mask(mask, r, c) else 0)
        _write_format(grid, version, level, mask)
        s = penalty(grid)
        if best is None or s < best[0]:
            best = (s, grid, mask)
    return version, level, best[2], best[1]


def penalty(m):
    n = len(m)
    score = 0
    for line in list(m) + [list(col) for col in zip(*m)]:
        run, prev = 1, line[0]
        for v in line[1:]:
            if v == prev:
                run += 1
            else:
                if run >= 5:
                    score += 3 + (run - 5)
                run, prev = 1, v
        if run >= 5:
            score += 3 + (run - 5)
        s = "".join(map(str, line))
        score += 40 * (s.count("10111010000") + s.count("00001011101"))
    for r in range(n - 1):
        for c in range(n - 1):
            if m[r][c] == m[r][c + 1] == m[r + 1][c] == m[r + 1][c + 1]:
                score += 3
    dark = sum(sum(row) for row in m)
    score += 10 * (abs(dark * 100 / (n * n) - 50) // 5)
    return score


# ---------------------------------------------------------------- decoding
def decode(grid):
    """Read a module matrix back to text. Returns (text, version, level, mask)."""
    n = len(grid)
    version = (n - 17) // 4
    # format info (top-left copy)
    fbits = 0
    for i in range(0, 6):
        fbits |= grid[8][i] << i
    fbits |= grid[8][7] << 6
    fbits |= grid[8][8] << 7
    fbits |= grid[7][8] << 8
    for i in range(9, 15):
        fbits |= grid[14 - i][8] << i
    fbits ^= 0x5412
    # undo BCH: find the closest valid codeword
    best = min(range(32), key=lambda d: bin(_bch(d, 0x537, 11) ^ fbits).count("1"))
    level = EC_FROM_BITS[(best >> 3) & 3]
    mask = best & 7

    _, _, order = skeleton(version)
    bits = []
    for (r, c) in order:
        bits.append(grid[r][c] ^ (1 if _mask(mask, r, c) else 0))
    stream = [int("".join(map(str, bits[i:i + 8])), 2) for i in range(0, len(bits) - 7, 8)]

    ec_pb, groups = EC_SPEC[version][level]
    block_lens = [d for count, d in groups for _ in range(count)]
    total_data = sum(block_lens)
    data_cw = stream[:total_data]
    blocks = [[] for _ in block_lens]
    i, pos = 0, 0
    for i in range(max(block_lens)):
        for b, blen in enumerate(block_lens):
            if i < blen:
                blocks[b].append(data_cw[pos])
                pos += 1
    flat = [cw for b in blocks for cw in b]

    def take(val, nbits):
        return (val >> nbits) & 1, nbits

    buf = [(cw >> i) & 1 for cw in flat for i in range(7, -1, -1)]
    mode = 0
    for i in range(4):
        mode = (mode << 1) | buf[i]
    if mode != MODE_BYTE:
        raise ValueError(f"unsupported mode indicator {mode}")
    cc = 8 if version <= 9 else 16
    count = 0
    for i in range(4, 4 + cc):
        count = (count << 1) | buf[i]
    start = 4 + cc
    raw = bytes(int("".join(map(str, buf[start + 8 * k:start + 8 * k + 8])), 2) for k in range(count))
    return raw.decode("utf-8"), version, level, mask


# ---------------------------------------------------------------- output
def _inner(info):
    border = info["border"]
    n = len(info["modules"]) - 2 * border
    return [row[border:border + n] for row in info["modules"][border:border + n]]


def modules(text, level="M", version=None, border=4):
    version, level, mask, grid = matrix(text, level, version)
    n = len(grid)
    out = [[0] * (n + 2 * border) for _ in range(n + 2 * border)]
    for r in range(n):
        for c in range(n):
            out[r + border][c + border] = grid[r][c]
    return {"version": version, "level": level, "mask": mask, "modules": out, "border": border}


def to_png(info, path, scale=10):
    mods = info["modules"]
    dim = len(mods) * scale
    rows = []
    for y in range(dim):
        row = bytearray([0])
        for x in range(dim):
            row += b"\x00\x00\x00" if mods[y // scale][x // scale] else b"\xff\xff\xff"
        rows.append(bytes(row))
    raw = b"".join(rows)

    def chunk(tag, payload):
        return (len(payload).to_bytes(4, "big") + tag + payload
                + (zlib.crc32(tag + payload) & 0xFFFFFFFF).to_bytes(4, "big"))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", dim.to_bytes(4, "big") + dim.to_bytes(4, "big") + bytes([8, 2, 0, 0, 0]))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    with open(path, "wb") as fh:
        fh.write(png)
    return dim


def selftest():
    cases = ["https://concree.org/goin-digital/inscription",
             "https://concree.org/gd/atelier",
             "HELLO WORLD", "a", "https://t.co/x?q=1&r=2#frag",
             "https://concree.org/goin-digital/inscription?src=affiche&lang=fr&utm=maquette"]
    ok = True
    for text in cases:
        for level in ("L", "M", "Q", "H"):
            try:
                version, blocks, ecs = encode_blocks(text, level)
            except ValueError as exc:
                print(f"  skip {level}: {exc}")
                continue
            version, level_, mask, grid = matrix(text, level, version)
            got, v2, l2, m2 = decode(grid)
            ec_pb = EC_SPEC[version][level][0]
            rs_ok = all(_rs_ok(list(b) + list(e), ec_pb) for b, e in zip(blocks, ecs))
            good = got == text and (v2, l2, m2) == (version, level, mask) and rs_ok
            ok &= good
            print(f"  {'OK  ' if good else 'FAIL'} v{version}-{level} mask{mask} rs={'y' if rs_ok else 'n'} {text[:46]!r} -> {got[:46]!r}")
    print("selftest", "PASSED" if ok else "FAILED")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    text, out = sys.argv[1], sys.argv[2]
    scale = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    border = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    level = sys.argv[5] if len(sys.argv) > 5 else "M"
    info = modules(text, level, None, border)
    dim = to_png(info, out, scale)
    back = decode(_inner(info))
    assert back[0] == text, f"round-trip mismatch: {back[0]!r}"
    print(f"v{info['version']}-{info['level']} mask {info['mask']} -> {out} ({dim}x{dim}px, decoded OK)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
