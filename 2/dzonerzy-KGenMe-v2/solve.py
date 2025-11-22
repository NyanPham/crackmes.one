"""
PHASE 1: Check Serial

chunk_1
    contains exactly one of "KJL"
    contains exactly 4 numbers

    j_0 = 4

chunk_2
    (chunk_2[4] - '0') is even 
    so chunk_2[4] in ['0', '2', '4', '6', '8']

chunk_3
    is_alpha(chunk_3[0])
    is_alpha(chunk_3[1])
    is_num(chunk_3[2])
    is_num(chunk_3[3])

    chunk_3[0] - chunk_3[1] == (chunk_3[2]-'0') + (chunk_3[3]-'0')

chunk_4
    all chunk_4 are in ['0'-'9', 'a'-'z', 'A'-'Z']

chunk_5
    mutate j_0
     

    success: contains at least one of "HBTOP" || all numbers are odd



PHASE 2: Check username and serial
Hash both username and serial with the same compute_hash function.
r = (a + b) % constant

Run validate_combined_hashes
Run 3 functions to compute a constant -> key
check if the r == key


"""

def check_serial(serial):
    check_indices = [5, 11, 17, 23]
    
    assert len(serial) == 29

    for i in check_indices:
        assert serial[i] == '-'

    parts = serial.split('-')

    assert len(parts) == 5

    chk1 = parts[0]
    chk2 = parts[1]
    chk3 = parts[2]
    chk4 = parts[3]
    chk5 = parts[4]

    # check chunk 1
    assert sum(1 for char in chk1 if char.isdigit()) == 4
    assert sum(1 for char in chk1 if char in ('K', 'J', 'L')) == 1

    # check chunk 2
    assert int(chk2[4]) % 2 == 0

    # check chunk 3
    char1, char2, char3, char4, _ = chk3
    
    assert (char1.isalpha() and char2.isalpha() and char3.isdigit() and char4.isdigit()) == True
    assert ord(char1) - ord(char2) == int(char3) + int(char4)

    # check chunk 4
    assert chk4.isalnum()

    # check chunk 5
    assert (any(char in ('H', 'B', 'T', 'O', 'P') for char in chk5) or all(char.isdigit() and int(char) % 2 != 0 for char in chk5))

    print(chk1)
    print(chk2)
    print(chk3)
    print(chk4)
    print(chk5)


def hash_str(s, salt=0x1F, mod=0x3B9ACA07):
    _hash = 0
    tmp = 1


    for i in range(len(s)):
        c = ord(s[i])
        _hash = (_hash + ((c * tmp) % mod)) % mod 
        tmp = (tmp * salt) % mod
    
    return _hash

def to_64bit(n):
    return n & 0xffffffffffffffff

def compute1(a, b, c):
    ret = 1

    while b != 0:
        if b % 2 != 0:
            ret = (ret * a) % c
        a = a**2 % c
        b = b >> 1

    return ret

def compute2(n):
    
    x = 0xA5A5A5A5A5A5A5A5
    n = to_64bit(n ^ x)
    n = to_64bit(n << 13 | n >> 51)
    n = to_64bit(n >> 17 | n << 47)
    
    y = 0x5A5A5A5A5A5A5A5A
    n = to_64bit(n ^ y)
    n = to_64bit(n >> 11 | n << 53)

    z = 0x5851F42D4C957F2D
    n = to_64bit(to_64bit(n * z) % 0xffffffffffffffff)
 
    return n


def compute3(n):
    x = 0xC097EF87329E28A5

    n = to_64bit(to_64bit(n * x) % 0xffffffffffffffff)
    n = to_64bit(n << 11 | n >> 53)
    
    y = 0x5A5A5A5A5A5A5A5A
    n = to_64bit(n ^ y)
    n = to_64bit(n << 17 | n >> 47)
    n = to_64bit(n >> 13 | n << 51)
    
    z = 0xA5A5A5A5A5A5A5A5
    n = to_64bit(n ^ z)

    return n

def main():
    x = 0x0C005
    y = 0x3 
    z = 0x8003
    w = 0x3ff2

    v = compute1(w, z, x)
    v = compute2(v)
    v = compute3(v)
    
    usr_name = "nyanpham"
    serial = "K1234-BBBB2-JA543-DDDDD-HELLO"
    check_serial(serial)
    
    h1 = hash_str(list(usr_name))
    h2 = hash_str(list(serial))

    print("hash_usrname = ", end="")
    print(h1)
    print("hash_serial = ", end="")
    print(h2)

    combined = to_64bit((h1 + h2) % 0x3B9ACA07)
    print("combined_hash = ", end="")
    print(hex(combined))
    
    print("v = ", end="")
    print(hex(v))


    # check if combined == v

main()
