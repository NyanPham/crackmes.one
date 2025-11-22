def gen(a, b, c, d, e):
    if d == 0:
        e = (a + b + 0x2a) & 0xffffffffffffffff
        return e

    return e

def gen_setup():
    magic_num1 = 0x946E2553F
    magic_num2 = 0x82245E133
    a = (magic_num1 + magic_num2) & 0xffffffffffffffff
    b = magic_num2
    c = 5
    d = 0
    e = 0

    return gen(a, b, c, d, e)

def run():
    num = gen_setup()
    print(num)

run()
