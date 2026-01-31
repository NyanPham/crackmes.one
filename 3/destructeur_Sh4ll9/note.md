We get password from user, call it `pw`.

Use `pw` to decrypt the function subroutine `goodBoy` to valid instructions.

Use the whole 271 bytes of decrypted `goodBoy` to create a checksum, which is checked to be equal to magic number `m` or not? If yes, call the function `goodBoy` out (decrypted to valid instructions successfully). Otherwise, failed.

Done the analysis of `decrypt` subroutine.
TODO: static analyze the `createChecksum`

# Analyze the `createChecksum` subroutine:

The snippet:
```asm
mov     eax, [rbp+chksum]
and     eax, 1
neg     eax
mov     [rbp+msk], eax  
mov     eax, [rbp+chksum]
shr     eax, 1
mov     edx, eax        
mov     eax, [rbp+msk]
and     eax, 0EDB88320h 
xor     eax, edx
mov     [rbp+chksum], eax
``` 

is to compute a byte's worth of a CRC-32 (Cyclic Redundancy Check). 
To research more: IEEE 802.3 (Ethernet) polynomial, which is used in ZIP, PNG and GZIP formats.

Breaking it down:

1. The constant 0xED88320:
The standard CRC-32 polynomal constant is 0x04C11DB7. and 0x#D88320 is the reversed version of it (LSB-frist). That means the snippet is to process bits in Little Endian order.

2. The logic analysis:

- LSB extraction & mask generation:
```asm
mov eax, [rbp+chksum]
and eax, 1          ; Get the Least Significant Bit (LSB)
neg eax             ; Negate it
mov [rbp+msk], eax  ; it's the mask
```

this results in either 0x0 (all zeros), or 0xffffffff (all ones), which is a mased based on the last bit.

- The shift and the conditional XOR:
```asm
mov     eax, [rbp+chksum]
shr     eax, 1
mov     edx, eax        
mov     eax, [rbp+msk]
and     eax, 0EDB88320h
xor     eax, edx
```

This says: if the bit shifted out was 1, xor the shifted chksum value with the polynomial.

3. Summary:
Based on the binary, j is inited with 7, and runs until j < 0. Here is how it works in C
```C
for (int j = 7; j >= 0; j--)
{
    int msk = -(chksum & 1);
    chksum = (chksum >> 1) ^ (0xEDB88320 & msk);
}
```

Now we know the hard part, so the whole algorithm of the `createChecksum` is this:
```c
int createChecksum(const char* buf)
{
    uint32_t chksum = 0xFFFFFFFF;
    while (*buf != '\0')
    {
        c = *buf++;
        chksum ^= c;
        for (int8_t i = 7; i >= 0; i--)
        {
            int msk = -(chksum & 1);
            chksum = (chksum >> 1) ^ (0xEDB88320 & msk);
        }
    }
    return chksum;
}
```
