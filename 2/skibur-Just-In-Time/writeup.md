# Just In Time

https://crackmes.one/crackme/63c4ee1a33c5d43ab4ecf49a

## Writeup

As we reverse the distributed executable, we will notice that it is calling `time` and `localtime` function, and storing its result to somewhere.

```
; at 0x142E
lea     rax, [rbp+timer]
mov     rdi, rax        ; timer
call    _time
lea     rax, [rbp+timer]
mov     rdi, rax        ; timer
call    _localtime
mov     cs:tm_struct, rax
```

Also, we can guess that function at 0x138A is for reading the user's input, because it is calling `fgets` function, by passing stdin as a stream.

```
; at 0x13F4
mov     rdx, cs:stdin   ; stream
mov     rax, [rbp+var_38]
mov     esi, 18h        ; n
mov     rdi, rax        ; s
call    _fgets
```

Address to the buffer of input data will be passed to function at 0x11BA.
We can easily understand that this function is validating if password is correct or not, because it does some bit shift operation against each characters inside input data, and compares with hardcoded value.

```
; at 0x1232
; TL;DR : input[0xB] << 2 != 0xC4 then incorrect
mov     rax, [rbp+input]
add     rax, 0Bh
movzx   eax, byte ptr [rax]
movsx   eax, al
shl     eax, 2
cmp     eax, 0C4h
jnz     incorrect
```

Lets run a loop to see which character is expected to be a password.

```py
>>> for i in range(0x100):
...     if i << 2 == 0xC4:
...             print(chr(i))
...
1
```

8 characters of password can be obtained by going through this procedure few times.
But tricky part starts here.

```
; at 0x129F
; input[1] << var_8 != 0xC8 then incorrect
mov     rax, [rbp+input]
add     rax, 1
movzx   eax, byte ptr [rax]
movsx   edx, al
mov     eax, [rbp+var_8]
mov     ecx, eax
shl     edx, cl
mov     eax, edx
cmp     eax, 0C8h
jnz     incorrect
```

Lets see whats the value inside `var_8` variable.

```
; at 0x11C9
mov     rax, cs:tm_struct
mov     ecx, [rax]
movsxd  rax, ecx
imul    rax, 66666667h
<snip.>
add     eax, ecx
sub     edx, eax
mov     [rbp+var_8], edx
```

Program is referencing tm structure (result of `localtime` function), and calculating somekind of value based on it.
By executing the program via debugger few times, we will notice that `var_8` can contain 0 or 1 or 2, and value will change per second.

Lets check the assembly code at 0x129F again.
Since `0xC8` represents non-printable character, when value inside `var_8` is 0, challenge should be not solvable.
Also, we will notice that when `var_8` is 2, challenge is not solvable, because if we shift 2 bits of printable character to left, it will become non-printable.
To summarize, `var_8` must be 1, to make the challenge  solvable.

Now, obtain the rest of characters in password.
Password should be `%djk(9^{.f@1F4?`.

I have reversed the logic, and wrote a python script that identifies when can program correctly validate the password (sorry for the dirty code).

```py
for sec in range(60):
    ax = sec
    cx = sec
    ax *= 0x66666667
    ax = ax >> 0x20
    ax = ax >> 2
    si = cx
    si = si >> 0x1f
    ax = ax - si
    dx = ax
    ax = dx
    ax = ax << 2
    ax = ax + dx
    ax = ax + ax
    dx = cx
    dx = dx - ax
    ax = dx
    ax = ax * 0x55555556
    ax = ax >> 0x20
    cx = dx
    cx = cx >> 0x1F
    ax = ax - cx
    var_8 = ax
    cx = var_8
    ax = cx
    ax = ax + ax
    ax = ax + cx
    dx = dx - ax
    var_8 = dx
    if var_8 == 1:
        print('"'+str(sec)+'"', end=' ')
```

In addition, I have wrote simple bash script which throws password to the program when it is solvable.

```sh
#!/bin/bash

solvable_sec=("1" "4" "7" "11" "14" "17" "21" "24" "27" "31" "34" "37" "41" "44" "47" "51" "54" "57")

while true
do
    current_sec=$(date +"%S")
    if [[ " ${solvable_sec[*]} " =~ " ${current_sec} " ]]; then
        echo -n "%djk(9^{.f@1F4?" | ./ski000 
        break
    fi
done
```

Run the script, and challenge will get solved.

```
$ ./solve.sh 
Enter password: Correct password.  Congratulation!
```

## String Decoder (Extra)

Encoded string inside the executable can be decoded by writing string decoder like below.

```py
def string_decoder(s: bytes) -> str:
    result = ''
    for i in range(len(s)):
        result += chr((s[i] >> 1) - 5)
    return result
```

As an example, lets decode encoded string stored inside rax / rdx register at 0x1397 / 0x13A1.

```
mov     rax, 0CCEA4AEED4F2E694h ; "Enter password: "
mov     rdx, 4A7ED2EEE8F8F0F0h
```

Pack the value to bytes, and pass it to the string decoder function.

```py
>>> import struct
>>>
>>> s = struct.pack('<Q', 0xCCEA4AEED4F2E694)
>>> s += struct.pack('<Q', 0x4A7ED2EEE8F8F0F0)
>>>
>>> string_decoder(s)
'Enter password: '
```

Other strings can be also decoded by same procedure.