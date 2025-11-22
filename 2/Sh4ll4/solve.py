def get_str(p1, p2, p3):
    bytes1 = p1.to_bytes(8, byteorder='little')
    bytes2 = p2.to_bytes(8, byteorder='little')
    bytes3 = p3.to_bytes(4, byteorder='little')
    full_bytes = bytes1 + bytes2 + bytes3
    string = full_bytes.split(b'\x00')[0].decode('ascii')
    return string

def get_a():
    part1 = 0x317A39683461617A  # 8 bytes
    part2 = 0x3167356167386167  # 8 bytes
    part3 = 0x347A3868          # 4 bytes

    return get_str(part1, part2, part3) 

def get_b():
    part1 = 0x7A31346861383165  # 8 bytes
    part2 = 0x7A35306861316838  # 8 bytes
    part3 = 0x67683961          # 4 bytes

    return get_str(part1, part2, part3) 

def get_c():
    part1 = 0x67346138687A327A  # 8 bytes
    part2 = 0x68397A3168613439  # 8 bytes
    part3 = 0x61613167          # 4 bytes

    return get_str(part1, part2, part3) 

def get_d():
    part1 = 0x4868396134684847  # 8 bytes
    part2 = 0x317A386B514A5A52  # 8 bytes
    part3 = 0x7A323168          # 4 bytes

    return get_str(part1, part2, part3) 

def run():
    a = get_a()
    b = get_b()
    c = get_c()
    d = get_d()
    
    fmt_str = "142x142x121x1424421x" 
    
    pass_buf = []
    for i in range(len(fmt_str)):
        c = fmt_str[i]
        if c == "1":
            pass_buf.append(b[i])
        elif c == "2":
            pass_buf.append(a[i])
        elif c == "3":
            pass_buf.append(c[i])
        elif c == "4":
            pass_buf.append(d[i])
        else:
            pass_buf.append('S')

    print(''.join(pass_buf))



if __name__ == '__main__':
    run()
