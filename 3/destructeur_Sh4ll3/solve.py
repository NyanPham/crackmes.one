"""
zg = "zg2z8h4z2z"
s5 = "S5do7apOWcl``clx"

fail_str = "Incorrect password, ganbatte kudasai!"
succ_str = "Your password is correct!"

res0 = xor(fail_str, zg)
res1 = xor(succ_str, zg)
res2 = xor(res0, pw)
res3 = xor(res2, res1)

res3 == s5?

XOR is reversible: res0 and res1 are constants, we have what we need to get pw
res2 = xor(s5, res1)
pw = xor(res2, res0) 

==> pw = "C4rrect_P4ssw0rd"
"""


def xor(s1: str, s2: str) -> str:
    xored = ""
    j = 0

    for i in range(len(s1)):
        c = ord(s1[i])
        c = c ^ ord(s2[j])
        xored += chr(c)
        j = (j+1)%len(s2)

    return xored

def run():
    zg = "zg2z8h4z2z"
    s5 = "S5do7apOWcl``clx"

    fail_str = "Incorrect password, ganbatte kudasai!"
    succ_str = "Your password is correct!"
    
    res0 = xor(fail_str, zg)
    res1 = xor(succ_str, zg)
    
    res2 = xor(s5, res1)
    pw = xor(res2, res0)
    print(pw)
    
if __name__ == '__main__':
    run()

    
