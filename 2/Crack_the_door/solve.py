def get_password(username, a ,b):
    assert len(username) == 11
    password = []

    i = 0
    while (i < 12):
        tmp1 = (ord(username[i]) ^ (a[i] + 0x32)) % 100 + 65
        tmp2 = b[((9*i) + 5) % 12]
        password.append(chr(tmp1))
        password.append(chr(tmp2))
        i += 2

    return ''.join(password)
        

def run():
    a = [0x54, 0x48, 0x45, 0x50, 0x49, 0x52, 0x41, 0x54, 0x45, 0x49, 0x53, 0x5a]
    b = [0x3f, 0x2a, 0x2d, 0x2f, 0x35, 0x39, 0x37, 0x24, 0x3d, 0x23, 0x26, 0x40]
    username = "nyanphamdev"

    password = get_password(username, a, b)
    
    print("USERNAME: ", end="")
    print(username)

    print("PASSWORD: ", end="")
    print(password)


if __name__ == '__main__':
    run()
