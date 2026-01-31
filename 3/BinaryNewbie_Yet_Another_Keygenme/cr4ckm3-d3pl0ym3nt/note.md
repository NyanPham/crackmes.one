the keygenme requires username and filepath.

username must be a string of 10 ints. 
filepath must have the contents with chars length <= 50.


Todo: reanalyze the else case `# buf_len != username_len`
Here is the algorithm to check the contents of file:

```
// f_size is the contents' length, which must be <= 50
// buf is the contents ptr
c = 0
count = 0

while (count < f_size):
    c = buf[c]
    if not is_digit(c):
        return fail()
    else: 
        count += 1
        c = count

if count != f_size:
    return fail()

// To this point, we know that count must be equal to f_size 
// it's haftly pointer-chasing, but we actually checking the character in range (0, f_size).

If both username and file's contents are correct, then we come to the final verification stage: f_verify_username_and_file.

f_verify_username_and_file(Str_t* username, FileHandle* file_handle):
    username_len = username->len
    buf_len = file_handle->len 

    if (buf_len == username_len):
        if (username_len == 0) fail()
        tmp_c = file_hanlde->buf[0]
        if (tmp_c == username->str[0]):
            if (strcmp(username->str, file_handle->buf):
                fail()

        total_sum = 0
        i = 0
        total_product = 1
        fc1 = file_handle->buf[1]
        fc2 = file_handle->buf[2]
        fc3 = file_handle->buf[3]
        fc4 = file_handle->buf[4]
        fc5 = file_handle->buf[5]
        fc6 = file_handle->buf[6]
        fc7 = file_handle->buf[7]
        fc8 = file_handle->buf[8]
        
        while (i != 10):
            c = username->str[i]
            m = (c + i) ^ i
            tc = (tmp_c ^ c) 0xF
            t1 = ((c ^ fc1) ^ 1) & 0xF
            t2 = ((c ^ fc2) ^ 2) & 0xF
            t3 = ((c ^ fc3) ^ 3) & 0xF
            t4 = ((c ^ fc4) ^ 4) & 0xF
            t5 = ((c ^ fc5) ^ 5) & 0xF
            t6 = ((c ^ fc6) ^ 6) & 0xF
            t7 = ((c ^ fc7) ^ 7) & 0xF
            t8 = ((c ^ fc8) ^ 8) & 0xF
            
            total_sum += tc + t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8
            total_product *= (tc | m) * (tc1 | m) * (tc2 | m) * (tc3 | m) * (tc4 | m) * (tc5 | m) * (tc6 | m) * (tc7 | m) * (tc8 | m)
        
        r = total_product % total_sum
        r = (r * 5) & 0xF
        if (r != 0):
            fail()
        else:
            success()

    else:
        # buf_len != username_len
        if (buf_len == 0):
            fail()
        
        
        s = 0
        p = 1

        for (i = 0; i < buf_len; i++):
            c = file_handle->buf[i]
            c1 = c
            for (j = 0; j < username_len; j++):
                x = username[j]
                x = (x + (c ^ j)) & 0xF
                s += x*2
                t = x | (c1 | (i ^ j))
                p *= t
                c1 += 1 

        r = (p - s) % (p + s)
        r &= 0xF
        r2 = 9 % r

        if (r2 != 0):
            fail()
        if (r != 0):
            success()
            
```

Look at the pseudo-code, at the end, the easiest path to find the password is the else case "buf_len != username_len". 
Because the algorithm involves bit-ops like ORing and XORing, so it's best to replicate the algorithm in Python to
bruteforce password for a fixed username. Please read `solve.py`.
