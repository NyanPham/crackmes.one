import sys
import os

# Add path for my_lib
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_path)

FILE_NAME = "sh4ll9.bin"
OUTPUT_NAME = "goodBoy_extracted.bin"
BYTE_COUNT = 271

# This is the hex signature of the start of your goodBoy function
# sub al, 27h; cld; xchg eax, esi
GOODBOY_SIGNATURE = b'\x2c\x27\xfc\x96'

def main():
    if not os.path.exists(FILE_NAME):
        print(f"[-] Error: {FILE_NAME} not found.")
        return

    with open(FILE_NAME, 'rb') as f:
        content = f.read()
        
        # Search for the function signature in the file
        offset = content.find(GOODBOY_SIGNATURE)
        
        if offset == -1:
            print("[-] Error: Could not find the goodBoy signature in the binary!")
            return
            
        print(f"[+] Found goodBoy function at File Offset: {hex(offset)}")
        
        # Extract the bytes
        data = content[offset : offset + BYTE_COUNT]
        
        with open(OUTPUT_NAME, 'wb') as out:
            out.write(data)
            
        print(f"[+] Successfully extracted {len(data)} bytes to {OUTPUT_NAME}.")

if __name__ == "__main__":
    main()
