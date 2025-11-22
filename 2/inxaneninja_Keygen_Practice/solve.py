def run():
    _str = input("Enter a str: ")
    _str_len = len(_str)
    acc = 0
    
    for i in range(_str_len):
        c = ord(_str[i])
        x = c * (_str_len**2)
        acc += x

    print(x)
    print(0xcdaa)

run()


