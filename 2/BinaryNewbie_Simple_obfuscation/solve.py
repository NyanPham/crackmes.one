"""
input string has length of 10
"""

def chk(s):
    buf = list("abcdefghij")
    s = list(s)
    assert len(buf) == 10
    #assert len(s) == 10
    
    buf_off = 0
    iter_cnt = len(s) - 1

    while buf_off < len(s):
        j = 0
    
        while j < iter_cnt:
            a = buf[buf_off]
            b = buf[j]

            buf[buf_off] = b
            buf[j] = a
            j = j + 1

        buf_off = buf_off + 1
  
    # buf now is jcdefghiab
    j = 0
    k = 0

    for i in range(len(s)):
        k -= 1 if s[i] == buf[i] else 0

    magic_num = 0xDEADBEEF
    magic_num >>= len(s)
    magic_num &= 0xc
    k ^= magic_num
    x = 4 - k
    print(x)

def run():
    s = input("String: ")

    chk(s)

run()
