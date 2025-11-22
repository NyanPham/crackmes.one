"""
pw_buf = ".-8.4.p"

"""


def run():
    pw_buf = ".-8.4.p"

    for i in range(7):
        c = (pw_buf[i])
        print(chr(ord(c) ^ ord('B')), end='')

run()
