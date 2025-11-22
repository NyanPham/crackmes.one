import struct

def run():
    a = 0x6C6830726E68656F
    b = 0x3A3E3E3B396B306A
    c = 0x303D6C3A3C3D303E
    d = 0x6F6C3E3B3D303131
    e = 0x3E6C3E6C
    f = 0x746B

    data = struct.pack('<QQQQIH', a, b, c, d, e, f)
    raw = data.split(b'\x00', 1)[0]
    
    for i in range(len(raw)):
        print(chr(raw[i] ^ 9), end="")

    print('\n')

if __name__ == '__main__':
    run()
