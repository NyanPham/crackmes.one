def accum_s_val(s):
    ret = 0
    for i in range(len(s)):
        ret += ord(s[i])

    return ret

def run():
    fname = "./keygenme"
    name = "nyanpham"

    acc = accum_s_val(name)
    key = (acc ^ (3*ord(name[0]))) << len(fname)
    print(key)


run()

