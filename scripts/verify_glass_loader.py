#!/usr/bin/env python3
"""Verify compiled loader NPDM permissions needed by GPU glass overlays."""
import struct
import sys
from pathlib import Path

def files(data):
    assert data[:4] == b'PFS0', 'not PFS0'
    n, names_size = struct.unpack_from('<II', data, 4)
    names = 16 + n * 24
    start = names + names_size
    result = {}
    for i in range(n):
        off, size, name_off = struct.unpack_from('<QQI', data, 16 + i * 24)
        name = data[names + name_off:data.index(b'\0', names + name_off)].decode()
        assert start + off + size <= len(data), 'truncated PFS0'
        result[name] = data[start + off:start + off + size]
    return result

npdm = files(Path(sys.argv[1]).read_bytes())['main.npdm']
assert npdm[:4] == b'META', 'not NPDM'
a, az, d, dz = struct.unpack_from('<IIII', npdm, 0x70)
assert struct.unpack_from('<I', npdm, d + 0x20c)[0] == 5, 'Applet memory pool required'
for offset, size, field in [(a, az, 0x30), (d, dz, 0x230)]:
    blob = npdm[offset:offset + size]
    co, cs = struct.unpack_from('<II', blob, field)
    caps = struct.unpack_from('<%dI' % (cs // 4), blob, co)
    assert 0x9fff in caps, 'Applet program type missing'
    assert any(caps[i:i+2] == (0x02a1003f, 0x0000403f) for i in range(len(caps)-1)), 'display MapRange missing'
print('Verified Applet program/pool and display MapRange in ACI0 and ACID.')
