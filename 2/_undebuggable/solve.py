"""
Disassembly of section .data:

00000000 <.data>:
   0:   55                      push   rbp
   1:   48 89 e5                mov    rbp,rsp
   4:   48 83 ec 40             sub    rsp,0x40
   8:   ba 20 00 00 00          mov    edx,0x20
   d:   48 8d 74 24 08          lea    rsi,[rsp+0x8]
  12:   bf 00 00 00 00          mov    edi,0x0
  17:   b8 01 00 00 00          mov    eax,0x1
  1c:   0f 05                   syscall
  1e:   be b6 03 00 00          mov    esi,0x3b6
  23:   bf 37 13 00 00          mov    edi,0x1337
  28:   b8 3e 00 00 00          mov    eax,0x3e
  2d:   0f 05                   syscall
  2f:   48 89 44 24 28          mov    QWORD PTR [rsp+0x28],rax
  34:   48 c7 04 24 01 00 00    mov    QWORD PTR [rsp],0x1
  3b:   00 
  3c:   b9 00 08 00 00          mov    ecx,0x800
  41:   ba 20 00 00 00          mov    edx,0x20
  46:   48 89 e6                mov    rsi,rsp
  49:   48 8b 7c 24 28          mov    rdi,QWORD PTR [rsp+0x28]
  4e:   b8 3d 00 00 00          mov    eax,0x3d
  53:   0f 05                   syscall
  55:   41 b8 00 00 00 00       mov    r8d,0x0
  5b:   b9 02 00 00 00          mov    ecx,0x2
  60:   ba 20 00 00 00          mov    edx,0x20
  65:   48 89 e6                mov    rsi,rsp
  68:   48 8b 7c 24 28          mov    rdi,QWORD PTR [rsp+0x28]
  6d:   b8 a5 00 00 00          mov    eax,0xa5
  72:   0f 05                   syscall
  74:   bf 05 00 00 00          mov    edi,0x5
  79:   b8 3f 00 00 00          mov    eax,0x3f
  7e:   0f 05                   syscall
  80:   ba ff 03 00 00          mov    edx,0x3ff
  85:   be 00 10 00 00          mov    esi,0x1000
  8a:   bf 39 05 00 00          mov    edi,0x539
  8f:   b8 02 00 00 00          mov    eax,0x2
  94:   0f 05                   syscall
  96:   48 89 44 24 28          mov    QWORD PTR [rsp+0x28],rax
  9b:   ba 00 00 00 00          mov    edx,0x0
  a0:   be 00 00 00 00          mov    esi,0x0
  a5:   48 8b 7c 24 28          mov    rdi,QWORD PTR [rsp+0x28]
  aa:   b8 2a 00 00 00          mov    eax,0x2a
  af:   0f 05                   syscall
  b1:   48 89 44 24 28          mov    QWORD PTR [rsp+0x28],rax
  b6:   be 01 00 00 00          mov    esi,0x1
  bb:   bf 01 00 00 00          mov    edi,0x1
  c0:   b8 0c 00 00 00          mov    eax,0xc
  c5:   0f 05                   syscall
  c7:   bf 05 00 00 00          mov    edi,0x5
  cc:   b8 6a 00 00 00          mov    eax,0x6a
  d1:   0f 05                   syscall
  d3:   48 8d 3d f9 02 00 00    lea    rdi,[rip+0x2f9]        # 0x3d3
  da:   48 8b 74 24 28          mov    rsi,QWORD PTR [rsp+0x28]
  df:   48 89 7c 24 30          mov    QWORD PTR [rsp+0x30],rdi
  e4:   b9 b0 00 00 00          mov    ecx,0xb0
  e9:   f3 a4                   rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]
  eb:   48 8d 74 24 10          lea    rsi,[rsp+0x10]
  f0:   48 8d 7c 24 08          lea    rdi,[rsp+0x8]
  f5:   48 8b 44 24 30          mov    rax,QWORD PTR [rsp+0x30]
  fa:   ff d0                   call   rax
  fc:   48 89 c6                mov    rsi,rax
  ff:   bf 02 00 00 00          mov    edi,0x2
 104:   b8 0c 00 00 00          mov    eax,0xc
 109:   0f 05                   syscall
 10b:   bf 05 00 00 00          mov    edi,0x5
 110:   b8 69 00 00 00          mov    eax,0x69
 115:   0f 05                   syscall
 117:   48 8d 3d f9 02 00 00    lea    rdi,[rip+0x2f9]        # 0x417
 11e:   48 8b 74 24 28          mov    rsi,QWORD PTR [rsp+0x28]
 123:   48 89 7c 24 30          mov    QWORD PTR [rsp+0x30],rdi
 128:   b9 b0 00 00 00          mov    ecx,0xb0
 12d:   f3 a4                   rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]
 12f:   48 8d 54 24 10          lea    rdx,[rsp+0x10]
 134:   48 8d 74 24 0c          lea    rsi,[rsp+0xc]
 139:   48 8d 7c 24 08          lea    rdi,[rsp+0x8]
 13e:   48 8b 44 24 30          mov    rax,QWORD PTR [rsp+0x30]
 143:   ff d0                   call   rax
 145:   48 89 c6                mov    rsi,rax
 148:   bf 03 00 00 00          mov    edi,0x3
 14d:   b8 0c 00 00 00          mov    eax,0xc
 152:   0f 05                   syscall
 154:   bf 05 00 00 00          mov    edi,0x5
 159:   b8 69 00 00 00          mov    eax,0x69
 15e:   0f 05                   syscall
 160:   48 8d 3d f9 02 00 00    lea    rdi,[rip+0x2f9]        # 0x460
 167:   48 8b 74 24 28          mov    rsi,QWORD PTR [rsp+0x28]
 16c:   48 89 7c 24 30          mov    QWORD PTR [rsp+0x30],rdi
 171:   b9 b0 00 00 00          mov    ecx,0xb0
 176:   f3 a4                   rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]
 178:   48 8d 4c 24 14          lea    rcx,[rsp+0x14]
 17d:   48 8d 54 24 10          lea    rdx,[rsp+0x10]
 182:   48 8d 74 24 0c          lea    rsi,[rsp+0xc]
 187:   48 8d 7c 24 08          lea    rdi,[rsp+0x8]
 18c:   48 8b 44 24 30          mov    rax,QWORD PTR [rsp+0x30]
 191:   ff d0                   call   rax
 193:   48 89 c7                mov    rdi,rax
 196:   b8 3c 00 00 00          mov    eax,0x3c
 19b:   0f 05                   syscall

"""


import struct

def build_shared_map():
    with open('undebuggable', 'rb') as fr:
        buf = fr.read()

    data = buf[0x3020:0x31bd]
   
    shared_map = []
    for i in range(0x19d):
        shared_map.append(data[i] ^ 0x55)

    return shared_map

def run():
    shared_map = build_shared_map()
    with open('decrypted_func', 'wb') as fw:
        fw.write(bytes(shared_map))
    
run()
