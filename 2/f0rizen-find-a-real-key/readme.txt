    ```
    $ r2 crackme
    s main
    af
    pdb
    ```
    Let's load sample and check first basic block of main function, local vars omitted
    ```
    ╭ 518: int main (int argc, char **argv);
    │                  ; arg int argc @ rdi
    │                  ; arg char **argv @ rsi
    ...
    │                  0x00001165      55             push rbp
    │                  0x00001166      4889e5         mov rbp, rsp
    │                  0x00001169      4881eca00000.  sub rsp, 0xa0
    │                  0x00001170      89bd6cffffff   mov dword [var_94h], edi ; argc
    │                  0x00001176      4889b560ffff.  mov qword [var_a0h], rsi ; argv
    │                  0x0000117d      64488b042528.  mov rax, qword fs:[0x28]
    │                  0x00001186      488945f8       mov qword [var_8h], rax
    │                  0x0000118a      31c0           xor eax, eax
    │                  0x0000118c      83bd6cffffff.  cmp dword [var_94h], 1
    │              ╭─< 0x00001193      7516           jne 0x11ab
    ```

    What we see here is check for number of arguments passed to the sample:
    In `edi` we can see nunmber of arguments.
    Register `rsi` contains "argv" or "argument vector". It is an array of string pointers
    that contains a list of strings.
    You cam read more about that in (here:)[http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html]

    So at addr `0x1170` variable var_94h gets argc.
    At addr `0x0118c` this value is being compared to 1.
    Mnemonic `jne` which is encoded as `75 cb`, cb stands for conditional byte. (reference)[https://www.felixcloutier.com/x86/jcc]
    ```
     75 cb      | JNE rel8  | Jump short if not equal (ZF=0).
    ```
    In case if no arguments were provided to program, argc would be euqal to 1. Jump will not be performed,
    and next opcode would be executed. Let's check following basic block, bb for short:
    ```
    │                  0x00001195      488d3d680e00.  lea rdi, str.Usage:_._crackme_FLAG ; 0x2004 ; "Usage: ./crackme FLAG"
    │                  0x0000119c      e88ffeffff     call sym.imp.puts    ; int puts(const char *s)
    │                  0x000011a1      b801000000     mov eax, 1
    │              ╭─< 0x000011a6      e9aa010000     jmp 0x1355
    ```

    The `puts` function gets into argument `str.Usage` of that program, sets eax to 1 and jumps to 0x1355.
    At that addr we have:
    ```
    pd 5 @ 0x1355
    │                  0x00001355      488b4df8       mov rcx, qword [var_8h]
    │                  0x00001359      64482b0c2528.  sub rcx, qword fs:[0x28]
    │              ╭─< 0x00001362      7405           je 0x1369
    │              │   0x00001364      e8e7fcffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
    │              ╰─> 0x00001369      c9             leave
    ```
    Restore stack (canary)[https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/],
    and in case if it's ok, exit.

    Let's go back to first bb and see what happens if argc is more than 1:
    in this case code flow follows to `0x11ab`
    ```
    │                  0x000011ab      488b8560ffff.  mov rax, qword [var_a0h]
    │                  0x000011b2      4883c008       add rax, 8
    │                  0x000011b6      488b00         mov rax, qword [rax]
    │                  0x000011b9      4889c7         mov rdi, rax
    │                  0x000011bc      e87ffeffff     call sym.imp.strlen  ; size_t strlen(const char *s)
    │                  0x000011c1      4883f815       cmp rax, 0x15
    │              ╭─< 0x000011c5      7416           je 0x11dd

    ```
    At addr `0x11ab` into the rax regiter content of var_a0h is placed:
    `mov rax, qword [var_a0h]`. Variable var_a0h is `argv`, so here we're accessing it's first member,
    advancing one and dereferencing that, hence getting first argument of program.

    Usage message shows that `Usage: ./crackme FLAG`, so in this code, at addr `0x011b9` rax is pointing
    to the string FLAG, which was entered by user at the start of program.
    This is passed to the `strlen` function, which checks how long string is.
    Result stored into `rax`. At addr `0x011c1` it's immediately compared with `0x15`. So we know, that
    flag should be 0x15 in lengh, or 21 in decimal. (`?vi 0x15` converts it to decimal).

    In case if flag is not that long, code flows to bb at 0x011c7, which `puts` "Wrong flag" message and 
    jumps to `0x1355` which is way to exit.

    If flag is 0x15 characters long -- additional checks applied:
    ```
    │                  0x000011dd      488d05410e00.  lea rax, str.sup3r_s3cr3t_k3y_1337 ; 0x2025 ; "sup3r_s3cr3t_k3y_1337"
    │                  0x000011e4      48898578ffff.  mov qword [var_88h], rax
    │                  0x000011eb      c78570ffffff.  mov dword [var_90h], 0
    │              ╭─< 0x000011f5      eb2e           jmp 0x1225

    ```
    This is a for loop initialization: at addr 0x011dd rax contains str.sup3r_s3cr3t_k3y_1337, which later
    goes to `var_88h`, variable `var_90h` gets incremented by 1 each iteration, so it's commonly named `i`.

    ```
    // Example
    for (var i=0; i<10; i++)
        ...
    ```
    So what can we see in this loop? Let's take a look:
    ```
    pd 17 @ 0x000011dd
    │                  0x000011dd      488d05410e00.  lea rax, str.sup3r_s3cr3t_k3y_1337 ; 0x2025 ; "sup3r_s3cr3t_k3y_1337"
    │                  0x000011e4      48898578ffff.  mov qword [var_88h], rax
    │                  0x000011eb      c78570ffffff.  mov dword [var_90h], 0
    │              ╭─< 0x000011f5      eb2e           jmp 0x1225
    │             ╭──> 0x000011f7      8b8570ffffff   mov eax, dword [var_90h]
    │             ╎│   0x000011fd      4863d0         movsxd rdx, eax
    │             ╎│   0x00001200      488b8578ffff.  mov rax, qword [var_88h]
    │             ╎│   0x00001207      4801d0         add rax, rdx
    │             ╎│   0x0000120a      0fb600         movzx eax, byte [rax]
    │             ╎│   0x0000120d      83e822         sub eax, 0x22
    │             ╎│   0x00001210      89c2           mov edx, eax
    │             ╎│   0x00001212      8b8570ffffff   mov eax, dword [var_90h]
    │             ╎│   0x00001218      4898           cdqe
    │             ╎│   0x0000121a      885405e0       mov byte [rbp + rax - 0x20], dl
    │             ╎│   0x0000121e      838570ffffff.  add dword [var_90h], 1
    │             ╎│   ; CODE XREF from main @ 0x11f5(x)
    │             ╎╰─> 0x00001225      83bd70ffffff.  cmp dword [var_90h], 0x14
    │             ╰──< 0x0000122c      7ec9           jle 0x11f7
    ```
    After it was initialized, execution flow follows to 0x1225, where our `i` variable is compared to 0x14,
     that is, 0x15-1, which is extra byte, 0x00 at the end of the string.
    If `var_90h` less than 0x15 execution flow jumps to 0x11f7
    Let's rename var_90h to i with help of this command: `afvn i var_90h`

    Now we can take a look at this cycle, step by step:
    ```
    0x11f7:
        eax = i
	rdx = eax		; i
	rax = &str.sup3r_s3cr3t_k3y_1337
	rax = rax + rdx		; 0th char in sup3r_s3cr3t_k3y_1337 + rdx (i)
	rax = (*byte)rax	; get byte
	rax = rax - 0x22	; substract 0x22
	edx = eax
	eax = i			; retrieve i
	rax = (word)eax		; extend i to word
    0x1210:
	; arr[i] = al		; save result from al to prepared memory addr
	rax = rax + 1		; increment counter
	jmp to 0x11f7 if i < 0x15
    ```

    In this cycle each char of string "sup3r s3cr3t k3y 1337" is getting substracted 0x22 and
    saved to the array on stack.

    After this loop, starting at address 0x0122e we can see another one array initialization,
      until address 0x012c1 with setting trailing zero to string.

    Next goes another loop.
    Variable var_8ch could be renamed to j via command `afvn j var_8ch`.
    ```
       ╭─< 0x000012cb      eb58           jmp 0x1325           ;[2]
      ╭──> 0x000012cd      488b8560ffff.  mov rax, qword [var_a0h]	; argv
      ╎│   0x000012d4      4883c008       add rax, 8			; first argument
      ╎│   0x000012d8      488b10         mov rdx, qword [rax]		; rdx contains entered key
      ╎│   0x000012db      8b8574ffffff   mov eax, dword [j]		; it is loop counter, j
      ╎│   0x000012e1      4898           cdqe
      ╎│   0x000012e3      4801d0         add rax, rdx
      ╎│   0x000012e6      0fb610         movzx edx, byte [rax]		; key
      ╎│   0x000012e9      8b8574ffffff   mov eax, dword [j]		; counter
      ╎│   0x000012ef      4898           cdqe
      ╎│   0x000012f1      0fb64405e0     movzx eax, byte [rbp + rax - 0x20] ; in eax transformed hardcoded key
      ╎│   0x000012f6      31d0           xor eax, edx			; xor transformed key's char and input
      ╎│   0x000012f8      0fbed0         movsx edx, al			; store result into edx
      ╎│   0x000012fb      8b8574ffffff   mov eax, dword [j]
      ╎│   0x00001301      4898           cdqe
      ╎│   0x00001303      8b448580       mov eax, dword [rbp + rax*4 - 0x80]
      ╎│   0x00001307      39c2           cmp edx, eax			; compare with
     ╭───< 0x00001309      7413           je 0x131e            ;[3]
     │╎│   0x0000130b      488d3d080d00.  lea rdi, str.Wrong_flag    ; 0x201a ; "Wrong flag"
     │╎│   0x00001312      e819fdffff     call sym.imp.puts    ;[4] ; int puts(const char *s)
     │╎│   0x00001317      b801000000     mov eax, 1
    ╭────< 0x0000131c      eb37           jmp 0x1355           ;[5]
    │╰───> 0x0000131e      838574ffffff.  add dword [j], 1
    │ ╎│   ; CODE XREF from main @ 0x12cb(x)
    │ ╎╰─> 0x00001325      83bd74ffffff.  cmp dword [j], 0x14
    │ ╰──< 0x0000132c      7e9f           jle 0x12cd           ;[6]
    ```

    So what do we see in that loop?
    First of all, the key user supplied is passed to the rax at addr 0x012cd,
    then first element (first char) is accessed. And that's placed to rdx.
    Next, loop counter j is placed into eax at address 0x012e9.
    At address 0x12f1 into eax, zero extended, loaded data which was placed before, at address 0x0121a,
    so in this address stored altered key char, a sup3r_s3cr3t_k3y_1337 - 0x22 for each byte.
    Then, this byte is being xor'ed with what user enters, at address 0x12f6.
    So at the end, this xored byte is being compared wtih users' input. Byte by byte. In cease if all of
    0x14 bytes are the same, crackme prints "You found a flag" string, and shows that entered flag.
    In case of first byte is different from expectable crackme shows "Wrong flag" message, and exits.

    Having all that, we can calculate expectable flag, only because XOR was used as an obfuscation mechanism.

    In order to get correct flag we need to do the calculations: From each byte of string "sup3r_s3cr3t_k3y_1337"
    we have to extract 0x22, then each of that altered bytes have to be xor'ed with expecting bytes.
    We can get this key with help of that python script:

    ```
    expected_key = ['0x37', '0x3f', '0x2f', '0x76', '0x2b', '0x62', '0x28',
	'0x21', '0x34', '0xf', '0x77', '0x62',  '0x48', '0x27',
	'0x75', '0x8', '0x56', '0x6a', '0x68', '0x4e', '0x68']

    key_str = 'sup3r_s3cr3t_k3y_1337'
    altered_key = [ord(ch)-0x22 for ch in key_str]
    flag = []
    # Convert key to bytes
    expected_key = [int(x, 16) for x in expected_key]
    for idx, ch in enumerate(altered_key):
	flag.append(chr(altered_key[idx] ^ expected_key[idx]))

    print(''.join(flag))
    # flag{_y0u_f0und_key_}
    ```

    Let's try that flag:
    ```
    $ ./crackme flag{_y0u_f0und_key_}
    You found a flag! flag{_y0u_f0und_key_}
    ```

