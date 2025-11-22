#!/usr/bin/env python3
import struct
import uuid

def decode_byte_to_char(byte):
    return chr((byte >> 1) - 5)

def print_success():
    a = 0x4AF2D0D4EEEEE890
    b = 0xD2EEE8F8F0F0CCEA
    c = 0xEED8E6E8904A4A66
    d = 0xE8DCF2CCE2F4F2CC
    e = 0x4CE6

    data = struct.pack('QQQQH', a, b, c, d, e)
    raw = data.split(b'\x00', 1)[0]

    chars = []
    for i in range(len(raw)):
        chars.append(decode_byte_to_char(raw[i]))

    print("".join(chars))


def print_failure():
    a = 0xD0D4EEEEE8D0E69C
    b = 0xE8F8F0F0CCEA4AF2
    c = 0x66D2EE
    
    data = struct.pack('<QQI', a, b, c)
    raw = data.split(b'\x00', 1)[0]

    chars = []
    for i in range(len(raw)):
        chars.append(decode_byte_to_char(raw[i]))
    
    print("".join(chars))
        

def get_usr_str():
    rax = 0xCCEA4AEED4F2E694
    rdx = 0x4A7ED2EEE8F8F0F0

    data = struct.pack('<QQ', rax, rdx)
    raw = data.split(b'\x00', 1)[0] 
    
    chars = []
    for i in range(len(raw)):
        chars.append(decode_byte_to_char(raw[i]))
    
    str = input("".join(chars))
    assert len(str) < 24

    return str

"""
0 1 2 3 4 5 6 7 8 9 A B C D
%djk(9^{.f@1F4
"""
def run():
    pass

if __name__ == "__main__":
    run()
