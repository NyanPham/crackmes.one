import struct

def run():
    s_vals = [0x62, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66, 0x31, 0x32]
    s2_vals = [0x10, 0x14, 0x0A, 0x05, 0x0C, 0x17, 0x0A, 0x02, 0x06]
    
    s = []
    for i in range(len(s_vals)):
        s.append((s_vals[i]))

    s2 = []
    for i in range(len(s2_vals)):
        s2.append((s2_vals[i]))


    s1 = []
    for i in range(len(s_vals)):
        s1.append(chr(s_vals[i] ^ s2_vals[i]))

    print("".join(s1))

run()
