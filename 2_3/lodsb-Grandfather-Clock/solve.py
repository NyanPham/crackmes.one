"""
The program needs 1 argument to run
The string param length must be even.
f_transform_str allocs another buf, and transform the str param into it through an algorithm.


TODO: a glimpse is that the returned trsf_str is compared with another buf. We're close ;)


transform_str algorithm:

i = 0
j = s_len - 1
magic_byte = 0xfe
new_str = []

while i < s_len:
    new_str[i] = str[j] - 0x20
    j += magic_byte
    if j == -1:
        j += 1
        magic_byte = -magic_byte

    i += 1


To revert:
i = s_len - 1
j = s_len - 2
magic_byte = 2

while i >= 0:
    str[j] = new_str[i] + 0x20
    j -= magic_byte
    if j == 0:
        j -= 1
        magic_byte = -magic_byte

    i -= 1
"""


def decrypt_bytes(data: bytes) -> str:
    """Subtract 0xC from each byte and return as ASCII string."""
    return ''.join(chr((b - 0xC) & 0xFF) for b in data)

def decrypt_bytes_2(data: bytes) -> str:
    return ''.join(chr((b >> 1) & 0xff) for b in data)

def print_usage(raw):
    start_offset = 0x2040
    end_offset   = 0x2050  # exclusive

    data = raw[start_offset:end_offset]
    decrypted = decrypt_bytes(data)
    print(decrypted)

def print_invalid_flag(raw):
    start_offset = 0x2060
    end_offset   = 0x2074  # exclusive

    data = raw[start_offset:end_offset]
    decrypted = decrypt_bytes_2(data)
    print(decrypted)

def print_valid_flag(raw):
    start_offset = 0x2080 
    end_offset   = 0x20a9

    data = raw[start_offset:end_offset]
    decrypted = decrypt_bytes_2(data)
    print(decrypted)

def get_cmp_str(raw):
    start_off = 0x2020
    end_off = 0x203c
    data = raw[start_off:end_off]
    return data

def retransform_buf(buf):
    print("PROCESSING ")
    org = [None] * len(buf)

    i = len(buf) - 1
    j = len(buf) - 2
    magic_byte = 2

    while i >= 0:
        org[j] = chr(buf[i] + 0x20)
        j -= magic_byte
        if j == 0:
            j -= 1
            magic_byte = -2

        i -= 1
   
    print(''.join(org[1:]))

def transform_str(str):
    print("PROCESSING 2")
    k = -2
    j = len(str) - 1

    for i in range(len(str)):
        print(hex(ord(str[j]) + 0x20),end='')
        j += k
        if j == -1:
            k = 2
            j = 0

def main():
    with open("grandfather_clock", "rb") as f:
        raw = f.read()
    
    data = get_cmp_str(raw)
    
    key = 'CTFlag{_H4rm0n1c_0sc1ll4t0r}'
    print(data)
    transform_str(key) 

    print_usage(raw)
    print_invalid_flag(raw)
    print_valid_flag(raw)

if __name__ == "__main__":
    main()

