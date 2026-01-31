import sys

def to_int32(n):
    """Simulate 32-bit signed integer overflow/underflow."""
    n = n & 0xFFFFFFFF
    if (n & 0x80000000):
        n = n - 0x100000000
    return n

def c_rem(a, b):
    """
    Emulate C-style remainder (truncates towards zero).
    Python's % operator floors, which gives different results for negatives.
    Example: 
      C:      -105 % 100 = -5
      Python: -105 % 100 = 95
    """
    return int(a - int(a / b) * b)

def parse(a, b, c):
    if b == 0:
        return None # Error state

    # Assembly: b < -4096 || b > 4096
    # Note: 0xFFFFF000 is -4096. jl checks strictly less than.
    if (b < -4096) or (b > 4096):
        # loc_1254: b = -(b % 4096)
        # Using C-style remainder
        rem = c_rem(b, 4096)
        b = -rem

    x = 1
    # Loop i from 0 to 2
    for i in range(3):
        # x ^= b << i
        # Must mask b to 32-bits before shifting to avoid infinite sign extension in Python
        shifted_b = ((b & 0xFFFFFFFF) << i) & 0xFFFFFFFF
        x = (x ^ shifted_b) & 0xFFFFFFFF

    # return (x + ((a + c - 1) ^ b) + a - 15)
    # All arithmetic must be 32-bit wrapped
    
    part1 = (a + c - 1) & 0xFFFFFFFF
    part2 = part1 ^ (b & 0xFFFFFFFF)
    
    # x + part2 + a - 15
    res = (x + part2 + a - 15) & 0xFFFFFFFF
    
    return to_int32(res)

def check_seed(seed):
    next_seed = seed
    
    # x = ((seed ^ 0x7b) + (seed ^ 0x141)) * 0x533d
    v1 = to_int32(seed ^ 0x7b)
    v2 = to_int32(seed ^ 0x141)
    x = to_int32(to_int32(v1 + v2) * 0x533d)
    
    # r = x % 100 (C-style remainder)
    # The assembly uses standard division magic to compute remainder
    r = c_rem(x, 100)
    
    # r = abs(r)
    if r < 0:
        r = -r
        
    # if r == 0: r = 10
    if r == 0:
        r = 10
        
    i = 0
    # loop while i <= 99 AND i < r
    while (i <= 99) and (i < r):
        res = parse(seed, next_seed, i)
        if res is None:
            return False # Invalid chain
        next_seed = res
        i += 1

    # Termination Checks (ASM loc_145B)
    
    # 1. If i == 99, we hit max iters -> Failure
    if i == 99:
        return False
        
    # 2. Loop exited. Success requires:
    #    - seed matches next_seed
    #    - i matches r (meaning we completed exactly r links)
    if seed == next_seed and i == r:
        print(f"\n[+] SUCCESS! Chain broken.")
        print(f"[+] Seed: {seed}")
        print(f"[+] Links (r): {r}")
        return True

    return False

def main():
    print("Brute-forcing seed... (Prioritizing negative range)")
    
    # 1. Search Negative range (as suspected)
    # Checking -10,000,000 to 0
    for s in range(-10000000, 1):
        if check_seed(s):
            return

    # 2. Search Positive range
    # Checking 0 to 10,000,000
    for s in range(1, 10000000):
        if check_seed(s):
            return

    print("Seed not found in standard range.")

if __name__ == '__main__':
    main()