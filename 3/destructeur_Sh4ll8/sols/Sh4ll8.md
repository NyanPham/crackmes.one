# destructeur's Sh4ll8

Opening this crackme in IDA does not give anything, it's obviously packed.
Let's play with the binary:

```
ltrace ./Sh4ll8
Couldn't find .dynsym or .dynstr in "/proc/22361/exe"
Welcome to Sh4ll8! Now, can you give me the password please: 
> [SUCCESS] T-That's impossible! You are so strong!
```

Well, pretty weird. No lib calls ?

```
~ strace ./Sh4ll8
execve("./Sh4ll8", ["./Sh4ll8"], [/* 52 vars */]) = 0
mmap(0x800000, 3791831, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, 0, 0) = 0x800000
readlink("/proc/self/exe", "/home/stan/Sh4ll8", 4096) = 17
mmap(0x400000, 3747840, PROT_NONE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x400000
mmap(0x400000, 1595335, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x400000
mprotect(0x400000, 1595335, PROT_READ|PROT_EXEC) = 0
mmap(0x785000, 36136, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0x185000) = 0x785000
mprotect(0x785000, 36136, PROT_READ|PROT_WRITE) = 0
mmap(0x78e000, 17224, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x78e000
munmap(0x801000, 3787735)               = 0
uname({sysname="Linux", nodename="forge", ...}) = 0
brk(NULL)                               = 0x1644000
brk(0x1645200)                          = 0x1645200
arch_prctl(ARCH_SET_FS, 0x16448c0)      = 0
readlink("/proc/self/exe", "/home/stan/Sh4ll8", 4096) = 17
brk(0x1666200)                          = 0x1666200
brk(0x1667000)                          = 0x1667000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 2), ...}) = 0
write(1, "Welcome to Sh4ll8! Now, can you "..., 62Welcome to Sh4ll8! Now, can you give me the password please: 
) = 62
write(1, "> ", 2> )                       = 2
fstat(0, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 2), ...}) = 0
read(0, abcde
"abcde\n", 1024)                = 6
ptrace(PTRACE_TRACEME)                  = -1 EPERM (Operation not permitted)
write(1, "What are you trying to do?\n", 27What are you trying to do?
) = 27
lseek(0, -1, SEEK_CUR)                  = -1 ESPIPE (Illegal seek)
exit_group(-6999)                       = ?
+++ exited with 169 +++
```

Ok. So the first syscalls are probably made by the packer in order to map memory and copy the real program. Then the program writes on STDOUT, read from STDIN, and call PTRACE. This is a classical anti-debugging method.

Let's hook this syscall in gdb.

```
gdb-peda$ catch syscall ptrace
Catchpoint 1 (syscall 'ptrace' [101])
gdb-peda$ r
Starting program: /home/stan/Sh4ll8 
Welcome to Sh4ll8! Now, can you give me the password please: 
> abcdefghijkl
[----------------------------------registers-----------------------------------]
RAX: 0xffffffffffffffda 
RBX: 0x400310 (sub    rsp,0x8)
RCX: 0x4f060e (cmp    rax,0xfffffffffffff000)
RDX: 0x1 
RSI: 0x0 
RDI: 0x0 
RBP: 0x7fffffffce40 --> 0x7fffffffcfa0 --> 0x78c018 --> 0x4d18c0 (pxor   xmm0,xmm0)
RSP: 0x7fffffffce38 --> 0x400ee0 (cmp    rax,0xffffffffffffffff)
RIP: 0x4f060e (cmp    rax,0xfffffffffffff000)
R8 : 0xffffffff 
R9 : 0x0 
R10: 0x0 
R11: 0x282 
R12: 0x499200 (push   r14)
R13: 0x499290 (push   rbx)
R14: 0x0 
R15: 0x7fffffffd3e0 --> 0x40000c (syscall)
EFLAGS: 0x282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4f0603:	cmova  r10,rcx
   0x4f0607:	mov    eax,0x65
   0x4f060c:	syscall 
=> 0x4f060e:	cmp    rax,0xfffffffffffff000
   0x4f0614:	ja     0x4f0640
   0x4f0616:	test   rax,rax
   0x4f0619:	js     0x4f0634
   0x4f061b:	cmp    r8d,0x2
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffce38 --> 0x400ee0 (cmp    rax,0xffffffffffffffff)
0008| 0x7fffffffce40 --> 0x7fffffffcfa0 --> 0x78c018 --> 0x4d18c0 (pxor   xmm0,xmm0)
0016| 0x7fffffffce48 --> 0x401459 (cmp    eax,0xffffffff)
0024| 0x7fffffffce50 --> 0x788720 --> 0x8 
0032| 0x7fffffffce58 --> 0x45ad09 (mov    rax,QWORD PTR [rsp+0x10])
0040| 0x7fffffffce60 --> 0x78fa60 --> 0x787080 --> 0x407730 (mov    rax,0x787070)
0048| 0x7fffffffce68 --> 0x7fffffffce70 --> 0x7a86f0 --> 0x2f7000002fe 
0056| 0x7fffffffce70 --> 0x7a86f0 --> 0x2f7000002fe 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Catchpoint 1 (call to syscall ptrace), 0x00000000004f060e in ?? ()
gdb-peda$
```

Ok, so let's modify the return value, then continue instructions by instructions.
We quickly arrive at the instruction

```
0x4014f6:	cmp    bl,al
```

Which is basically a comparaison one-byte at a time of our input.
Let's find the comparaison value.
The ebx (bl) value comes from here

```
0x4014d4:	mov    eax,DWORD PTR [rax] // with rax = 0x7a86f4
   0x4014d6:	xor    eax,0xffffffab
   0x4014d9:	add    eax,0xc
=> 0x4014dc:	mov    ebx,eax
```

What's at 0x7a86f4 ? 

```
gdb-peda$ x/30xw 0x7a86f0 
0x7a86f0:	0x000002fe	0x000002f7	0x000002fe	0x000002f7
0x7a8700:	0x000002f8	0x000002c9	0x000002c8	0x000002fd
0x7a8710:	0x000002c8	0x000002f3	0x000002c6	0x000002fc
0x7a8720:	0x000002fe	0x000002c9	0x000002fc	0x000002cd
0x7a8730:	0x000002fe	0x000002fc	0x000002f4	0x000002ca
0x7a8740:	0x000002f2	0x00000000	0x00000000	0x00000000
0x7a8750:	0x00000000	0x00000000	0x00000000	0x00000000
0x7a8760:	0x00000000	0x00000000
```

Let's find the password !

```python
a = [0x000002fe,0x000002f7,0x000002fe,0x000002f7,0x000002f8,0x000002c9,0x000002c8,0x000002fd,0x000002c8,0x000002f3,0x000002c6,0x000002fc,0x000002fe,0x000002c9,0x000002fc,0x000002cd,0x000002fe,0x000002fc,0x000002f4,0x000002ca, 0x000002f2]

for i in range(0,len(a)):
    print(chr(((a[i] ^ 0xffffffab) + 0xc ) & 0xff), end='')
```

```
~ python3 test.py
ahah_nobodycancrackme
➜  ~ ./Sh4ll8
Welcome to Sh4ll8! Now, can you give me the password please: 
> ahah_nobodycancrackme 
[SUCCESS] T-That's impossible! You are so strong!
```

Interesting crackme! However, there's a little bug in it: The program check the user input one byte at a time (and exit if the comparaison fail), but the program stop at the end of the user input!

Which mean that 

```
➜  ~ ./Sh4ll8
Welcome to Sh4ll8! Now, can you give me the password please: 
> a
[SUCCESS] T-That's impossible! You are so strong!
➜  ~ ./Sh4ll8
Welcome to Sh4ll8! Now, can you give me the password please: 
> ahah_
[SUCCESS] T-That's impossible! You are so strong!
➜  ~ ./Sh4ll8
Welcome to Sh4ll8! Now, can you give me the password please: 
> ahah_nob
[SUCCESS] T-That's impossible! You are so strong!
```

So you can just bruteforce the solution :)

