import sys
from pathlib import Path

base = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(base))

from my_lib.utils import parse_local_str

if __name__ == '__main__':
    vals = [
        0x75746172676E6F43,  # moved into rax then stored -> qword at s
        0x20736E6F6974616C,  # moved into rdx then stored -> var_28
        0x2064696420756F79,  # moved into rax then stored -> var_20
    ]

    succ_msg = parse_local_str(vals)
    print("SUCC_MSG: ", end="")
    print(succ_msg)
    indexes = 0x32B6E514
    s = [None] * 8

    for i in range(8):
        idx = indexes & 0x0F
        c = succ_msg[idx]
        s[i] = c
        indexes >>= 4

    print("".join(s))


