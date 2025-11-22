import os

def xor_files(file1_path, file2_path, output_path, chunk_size=4096):
    size1 = os.path.getsize(file1_path)
    size2 = os.path.getsize(file2_path)

    if size1 != size2:
        raise ValueError("Files must have same size")

    
    with open(file1_path, 'rb') as f1, \
        open(file2_path, 'rb') as f2, \
        open(output_path, 'wb') as fout:
        
        while True:
            chunk1 = f1.read(chunk_size)
            chunk2 = f2.read(chunk_size)

            if not chunk1:
                break
                
            xor_result = bytes(b1 ^ b2 for b1, b2 in zip(chunk1, chunk2))
            fout.write(xor_result)
    
    
        
def run():
    xor_files('key', 'XOR_REV(QWER=RIFF)', 'xor_res')

if __name__ == '__main__':
    run()
