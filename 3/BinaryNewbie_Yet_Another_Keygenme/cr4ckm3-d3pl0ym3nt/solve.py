import itertools
import string

def solve_crackme_better():
    USERNAME = b"0123456789"
    
    charset = string.ascii_letters + string.digits 
    
    print(f"Cracking for username: {USERNAME}")
    print(f"We only scan for alphanumeric (a-Z, 0-9)")
    
    MASK64 = 0xFFFFFFFFFFFFFFFF
    for length in range(12, 50): 
        print(f"Checking length {length}...")
        
        for candidate_tuple in itertools.product(charset.encode(), repeat=length):
            file_bytes = bytes(candidate_tuple)
            
            p = 1
            s = 0
            
            for i in range(len(file_bytes)):
                c = file_bytes[i]
                c1 = c
                for j in range(len(USERNAME)):
                    x = USERNAME[j]
                    x = (x + (c ^ j)) & 0xF
                    s = (s + (x * 2)) & MASK64
                    t = x | (c1 | (i ^ j))
                    p = (p * t) & MASK64
                    c1 += 1
            
            num = (p - s) & MASK64
            den = (p + s) & MASK64
            
            if den != 0:
                r = num % den
                r_masked = r & 0xF
                
                if r_masked != 0 and (9 % r_masked == 0):
                    print(f"\n[SUCCESS] :) Found password: '{file_bytes.decode()}'")
                    return

    print("No password found! :(")

if __name__ == "__main__":
    solve_crackme_better()
