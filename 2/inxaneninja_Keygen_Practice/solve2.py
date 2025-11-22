import string
from itertools import combinations_with_replacement

TARGET = 0xcdaa  # 52650
charset = [chr(c) for c in range(32, 127)]  # Printable ASCII characters

# Check all reasonable lengths where n^2 divides 52650
for n in range(1, 20):
    n_squared = n * n
    if TARGET % n_squared != 0:
        continue
    ascii_sum = TARGET // n_squared

    # Early cutoff: if target sum too small or large
    if ascii_sum < n * ord(min(charset)) or ascii_sum > n * ord(max(charset)):
        continue

    print(f"Trying length = {n}, target character sum = {ascii_sum}")

    # Try combinations with replacement to avoid crazy branching
    for combo in combinations_with_replacement(charset, n):
        if sum(ord(c) for c in combo) == ascii_sum:
            print("Found valid input:", ''.join(combo))
            exit()

print("No valid input found.")

