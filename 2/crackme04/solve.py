"""
217552398261569-545326772-1082328767-1082328760-1082328765-1082328753
"""


def load_buff():
    with open('crackme04_64bit_test', 'rb') as fr:
        buff = fr.read()
   
    data = buff[0xD5D:0xD66-1]
    return data

def oil(a, b):
    b ^= 4
    a ^= 0x2E39F3
    
    return a, b

def run(): 
    pid = 0x539
    key = 0x35478
    buff = load_buff()
    
    key_buff = []

    for i in range(7):
        tmp = buff[i]
        tmp += 0x5c
        key ^= pid 
        tmp += key
        key, tmp = oil(key, tmp)
        
        key_buff.append(tmp)
        key <<= 7 

    print(key_buff)
        

if __name__ == '__main__':
    run()
