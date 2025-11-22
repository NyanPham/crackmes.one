def load_buf():
    file_path = './muldimalph'
    
    start_offset = 0x2020
    end_offset = 0xa039
    buf_len = end_offset - start_offset
    with open(file_path, 'r') as f:
        f.seek(start_offset)
        buf = f.read(buf_len)
    
    return buf


def valid_char(char):
    return char > '/' and char <= 'z'

def validate_serial(serial, buf):
    if not valid_char(serial[0]) or not valid_char(serial[1]) or not valid_char(serial[2]):
        return False
    
    if not len(serial) == 16:
        return False

    div_0 = ord(serial[0]) / 122.0
    div_1 = ord(serial[1]) / 122.0
    div_2 = ord(serial[2]) / 122.0
    
    dest = []
    for i in range(3):
        dest.append(serial[i])
    
    
    for i in range(3, 16):
        a = int(2*i*div_2)
        b = int(2*i*div_1)
        c = int(2*i*div_0)

        j = (b + (a * 32)) * 32 + c
        dest.append(buf[j])

    print("Correct serial is: ", "".join(dest))
    return True

def main():
    serial = 'zzzdefghijklmpop'
    buf = load_buf()
    good = validate_serial(serial, buf)


if __name__ == '__main__':
    main()
