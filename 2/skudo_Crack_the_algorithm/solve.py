import struct

def create_key(s):
    s_len = len(s)
    buf = []
    val = 0

    for i in range(s_len):
        buf.append(ord(s[i]))
        val += buf[i]
   
    val = (((val + 0x99af) ^ val) ^ 0x834c) * 0x122b
    val &= 0xff

    ret = 0
    for j in range(s_len):
        buf[j] ^= val
        ret += buf[j]

    ret %= 100
    if ret < 0:
        ret *= -1
   
    return ret

def encrypt_byte(b, k):
    return b ^ k

def run():
    str_0 = "imsupersecur3"
    str_1 = "SvenJoergenIkeaBirdWaterSheepBoatCowPeePeePooPoo"
    str_1_len = len(str_1)
    
    key = create_key(str_0)
   
    int_buf = []
    
    for i in range(str_1_len):
        int_buf.append(ord(str_1[i]))

    f = open('key.txt', 'wb')

    for j in range(str_1_len):
        int_buf[j] = encrypt_byte(int_buf[j], key)
        key = int_buf[j]
        f.write(struct.pack('B', int_buf[j]))
  

    #fname = input("Enter the path of the file containing the key: ")
    
    #with open(fname, 'r') as f:
     #   lines = f.readlines()
      #  line = lines[0].strip()

    #print(line)
    #print(str_2)
    #if line == str_2:
     #   print("Congratulations! You cracked the code!")
    #else:
     #   print("Nope, it seems like you',27h,'re not able to crack it eh?")




run()
