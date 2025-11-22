def run():
    secret_key = list('sup3r_s3cr3t_k3y_1337')
    encoded_key = ['7', '?', '/', 'v', '+', 'b', '(', '!', '4', 0xf, 'w', 'b', 'H', '\'', 'u', 8, 'V', 'j', 'h', 'N', 'h']
    
    assert len(secret_key) == len(encoded_key)
    
    hash_arr = []
    
    for i in range(len(secret_key)):
        c = ord(secret_key[i])
        c -= 0x22
        hash_arr.append(c)
   
    inp_chrs = []

    for j in range(len(encoded_key)):
        a = encoded_key[j]
        if isinstance(a, str):
            a = ord(a)

        b = hash_arr[j]
        inp_chrs.append(chr(a ^ b))

    print("".join(inp_chrs))

run()
