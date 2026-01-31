import random

legal_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def check(name, data):

    if (not len(name) == 10) or (len(data) > 50):
        return False

    r9 = 0
    r10 = 1
    for k in range(len(data) - 1):
        for i in range(len(name)):
            val = (ord(name[i]) + (ord(data[k]) ^ i)) & 0xf
            val2 = (ord(data[k]) + i) | (i ^ k)
            r9 += val * 2
            r10 *= (val | val2)
            r10 &= 0xffffffffffffffff

    rcx = (r10 - r9) % (r9 + r10)
    if rcx % 0x10 in [1, 3, 9]:
        return True
    else:
        return False

def random_str(chars, n):
    s = ''.join([random.choice(chars) for _ in range(n)])
    return s

def find_passwd(name):
    candidate_len = 8
    for _ in range(100000):
        passwd = random_str(legal_char, candidate_len)
        if check(name, passwd):
            print(name, passwd)
            break


name = 'jf721hdp0q'
# passwd = 'abcdef'
# print(check(name, passwd))

find_passwd(name)

# abcdef works
# data = open('input', 'rb').read()

# r9 = check(name, data)
# print(hex(r9))

# possible_r9 = []
# for i in range(2, 2 * 0xf * 500 + 2):
#     ecx = (2 ** 32) % i
#     if ecx & 0xf in [1, 3, 9]:
#         possible_r9.append(i)

# print(possible_r9)

# ./keygenme 0123456789 input
# Another keygenme - A bit evil this time ahahah
# Find a correct password for your username...
# I hope that will be funny....
# Developed by Binary Newbie

# [+] Let's parse the given content......
# [+] Username was parsed...
# [+] File was parsed.....
# [+] Let's verify...
# [+] Status:
# [+] Username is: 0123456789
# [+] File content is: abcdef[+] Check your file "input"


# ('0123456789', 'EJUkSN3W')
# ('hevk9a3f7b', 'WBkNoN5U')
# ('jf721hdp0q', 'CpAD7tGq')