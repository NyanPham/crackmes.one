import sys

def to_int32(n):
    n = n & 0xFFFFFFFF
    if (n & 0x80000000):
        n = n - 0x100000000
    return n

def c_rem(a, b):
    return int(a - int(a / b) * b)

def parse(a, b, c):
    if (b == 0):
        return None
    
    # bound check to make sure -4096 < b < 4096
    if (b < -4096) or (b > 4096):
        rem = c_rem(b, 4096)
        b = -rem

    x = 1
    for i in range(3):
        shifted_b = ((b & 0xFFFFFFFF) << i) & 0xFFFFFFFF
        x = (x ^ shifted_b) & 0xFFFFFFFF

    part1 = (a + c - 1) & 0xFFFFFFFF
    part2 = part1 ^ (b & 0xFFFFFFFF)
    res = (x + part2 + a - 15) & 0xFFFFFFFF

    return to_int32(res) 

def check_seed(seed):
    next_seed = seed
    
    v1 = to_int32(seed ^ 0x7b)
    v2 = to_int32(seed ^ 0x141)
    x = to_int32(to_int32(v1 + v2) * 0x533d)

    r = c_rem(x, 100)

    if r < 0:
        r = -r

    if r == 0:
        r = 10

    i = 0
    while (i <= 99) and (i < r):
        res = parse(seed, next_seed, i)
        if res is None:
            return False
        next_seed = res
        i += 1

    if i == 99:
        return False
    
    if seed == next_seed and i == r:
        print(f"\n[+] SUCCESS! Chain broken.")
        print(f"[+] Seed: {seed}")
        print(f"[+] Links (r): {r}")
        return True

    return False


def main():
    print("Brute-forcing seed... (Prioritizing negative range)")

    for s in range(-100000, 1):
        if check_seed(s):
            return

    for s in range(1, 100000):
        if check_seed(s):
            return
        
    print("Seed not found in standard range.")

if __name__ == '__main__':
    main()
