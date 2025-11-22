def encr(name):
    name_len = len(name)
    val = 0

    for i in range(name_len):
        val += ord(name[i])

    quo = 0
    buf = []
    for j in range(9):
        quo = val // (name_len + j)
        val += val // quo
        buf.append(chr(quo))
    
    return ''.join(buf)
        

def run():
    #name = input('Enter name: ')
    name = 'NyanPham'
    key = encr(name)
    print(key)    

if __name__ == '__main__':
    run()
