# o day ta thay co goi ham ma hoa
# ta se viet code key gen o day

from typing import Sized


def encry(name):
    sum = 0
    c1 = 0
    key = ""
    for i in name:
        sum += ord(i)

    for j in range(0,9):
        c1 = sum // (len(name) + j)
        key += chr(c1)
        sum += (sum // c1)
    print('Key is '  + key)


encry('admin')
