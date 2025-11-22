def qword_to_bytes_le(x):
    """Convert a 64-bit integer into 8 little-endian bytes."""
    return bytes([(x >> (8*i)) & 0xff for i in range(8)])

def print_failure():
    # ----------------------------
    # First string (XOR with 0xE9)
    # ----------------------------
    arr1_qwords = [
        0x8C82C98E87869BBE,
        0x0C98C9FCEA0C9C890,
        0x878684C9878C8C9A,
        0x88849AC99A908C82,
        0x88819DC99B8C9D9B,
        0x0C7C7C79C8690C987,
    ]
    arr1_tail_word = 0x00E3
    arr1_tail_byte = 0x00

    raw1 = b''.join(qword_to_bytes_le(x) for x in arr1_qwords)
    raw1 += arr1_tail_word.to_bytes(2, 'little')
    raw1 += bytes([arr1_tail_byte])

    decoded1 = bytes([b ^ 0xE9 for b in raw1])
    
    print("First string:", decoded1.decode('latin1', errors='replace'))

def print_success():
    # ----------------------------
    # Second string (XOR with 0xF9)
    # ----------------------------
    arr2_qwords = [
        0x96A0D9D89D9696BE,
        0x8D90D98D969ED98C,
        0x988B9E97969AD9D5,
        0x9C8F98B1D9D7838D,
        0x908B8DD98C9680D9,
        0x9C92D9968DD99D9C,
        0x0C69C94D9979C9E80,
        0x8B9AD98D819CB7D9,
        0x968AD99C94929A98,
        0x0F3A7A6A7D99796,
    ]
    arr2_tail_byte = 0x00

    raw2 = b''.join(qword_to_bytes_le(x) for x in arr2_qwords)
    raw2 += bytes([arr2_tail_byte])

    decoded2 = bytes([b ^ 0xF9 for b in raw2])
    print("Second string:", decoded2.decode('latin1', errors='replace'))

# helper
def is_odd(n: int) -> bool:
    return n % 2 != 0

def is_even(n: int) -> bool:
    return not is_odd(n)

a = 0
b = 0
c = 0
d = 0
def init_vars(s: str): # loop_1
    global a
    global b
    global c
    global d
    for i in range(4):
        d = ord(s[i]) + d - 0x30
        c = ord(s[i+4]) + c - 0x30
        b = ord(s[i+8]) + b - 0x30
        a = ord(s[i+12]) + a - 0x30

def check_vars() -> bool:
    """
        a, d are odd
        5 < d <= 24 ; d [7, 9, 11, 13, 15, 17, 19, 21, 23]
        c > b
        2a + 2b == d + c ; d == a, c = 2b + a 
    """

    """
        a = 7
        d = 7
        b = 3
        c = 13
             d    c    b    a
        => "1123-3712-0012-2311"
    """

    global a, b, c, d 

    if 2*(a+b) != (d+c):
        return False
    if c <= b:
        return False
    if is_odd(d + a):
        return False
    if d <= 5 or d > 24:
        return False 
    if is_even(a):
        return False
    
    return True


if __name__ == "__main__":
    input_num = "1123371201202311"
    assert len(input_num) == 16

    init_vars(input_num)
    print("a = ", a, end="\n")
    print("b = ", b, end="\n")
    print("c = ", c, end="\n")
    print("d = ", d, end="\n")
     
    if (check_vars()):
        print_success()
    else:
        print_failure()

    
