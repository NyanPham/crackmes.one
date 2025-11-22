### Solution

First we checkout our Main as usual, and we notice this: 

```
  std::operator<<((basic_ostream *)std::cout,"\nPlease Enter The Password: ");
  std::basic_istream<char,std::char_traits<char>>::getline(std::cin,(long)inputStuff);
  xxx();  <<< ------------- This is very interesting.
  cVar1 = check_password(inputStuff); <<< ------------ This too :D 
```

Now, xxx(), checking it in disassembler we find following two things: 


```
  
  bVar4 = 0;
  strcat(pass,key3);
  uVar2 = 0xffffffffffffffff;
  pcVar3 = pass;
  do {
    if (uVar2 == 0) break;
    uVar2 = uVar2 - 1;
    cVar1 = *pcVar3;
    pcVar3 = pcVar3 + (ulong)bVar4 * -2 + 1;
  } while (cVar1 != '\0');
                    /* 0z4141 -> AA */
  *(undefined2 *)(~uVar2 + 0x1042df) = 0x4141;
  pass[~uVar2 + 1] = 0;
  strcat(pass,key2);
  strcat(pass,key9);
  uVar2 = 0xffffffffffffffff;
  pcVar3 = pass;
```

This poses the question to what is key(2,3,9), unfortunately inspection and modification of data type in r2 is difficult, which leads to a lots of misunderstanding
here we were able to modify the data type to TerminatedCstrings in ghidra, and that gives us: 
```
                             __dso_handle                                    XREF[4]:     Entry Point(*), 
                                                                                          __do_global_dtors_aux:00101147(R
                                                                                          __static_initialization_and_dest
                                                                                          00104048(*)  
        00104048 48 40 10        addr       __dso_handle                                     = 00104048
                 00 00 00 
                 00 00
                             key1                                            XREF[1]:     Entry Point(*)  
        00104050 48 65 6c        ds         "Hello"
                 6c 6f 00
                             key2                                            XREF[2]:     Entry Point(*), xxx:001012e6(*)  
        00104056 74 68 69        ds         "this"
                 73 00
                             key3                                            XREF[2]:     Entry Point(*), xxx:0010129b(*)  
        0010405b 69 73 00        ds         "is"
                             key4                                            XREF[1]:     Entry Point(*)  
        0010405e 41 00           ds         "A"
                             key5                                            XREF[1]:     Entry Point(*)  
        00104060 63 72 61        ds         "crackMe"
                 63 6b 4d 
                 65 00
                             key6                                            XREF[1]:     Entry Point(*)  
        00104068 66 72 6f        ds         "from"
                 6d 00
        0010406d 00              ??         00h
        0010406e 00              ??         00h
        0010406f 00              ??         00h
                             key7                                            XREF[1]:     Entry Point(*)  
        00104070 44 34 52        ds         "D4RK_FL0W"
                 4b 5f 46 
                 4c 30 57 00
                             key8                                            XREF[1]:     Entry Point(*)  
        0010407a 48 41 56        ds         "HAVE"
                 45 00
                             key9                                            XREF[2]:     Entry Point(*), xxx:001012f9(*)  
        0010407f 46 75 6e 00     ds         "Fun"

```


Which gives us: this is Fun, let's continue checking down the function as well as to whats happening, at this point I couldnt figure out how to get debugger running in ghidra, so I switched to r2, 
```
>>> r2 -d ./crack2-by-D4RK_FL0W   
>>> aaa
>>> afl
>>> s main 
│           0x556fe939b1b4      e833000000     sym.check_password_char_  () ; check_password(char*)
│           0x556fe939b1b9      84c0           var = al & al
│       ┌─< 0x556fe939b1bb      7415           if  (!var) goto loc_0x556fe939b1d2
│       │   0x556fe939b1bd      488d35640e00.  rsi = rip + str._n_nCorrect_You_Cracked_It_n ; 0x556fe939c028 ; "\n\n***Correct You Cracked It***\n"

check_password is interesting
>>> s sym.check_password_char_
[0x556fe939b175]> s sym.check_password_char_ 
[0x556fe939b1ec]> pdf
            ; CALL XREF from main @ 0x556fe939b1b4
┌ 77: sym.check_password_char_ (int64_t arg1);
│           ; var int64_t var_18h @ rbp-0x18
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           0x556fe939b1ec      55             push  (rbp)             ; check_password(char*)
│           0x556fe939b1ed      4889e5         rbp = rsp
│           0x556fe939b1f0      48897de8       qword [var_18h] = rdi   ; arg1
│           0x556fe939b1f4      c745fc000000.  dword [var_4h] = 0
│           ; CODE XREF from check_password(char*) @ 0x556fe939b230
│       ┌─> 0x556fe939b1fb      837dfc0f       var = dword [var_4h] - 0xf
│      ┌──< 0x556fe939b1ff      7f31           if  (var > 0) goto loc_0x556fe939b232
│      │╎   0x556fe939b201      8b45fc         eax = dword [var_4h]
│      │╎   0x556fe939b204      4863d0         rdx = eax
│      │╎   0x556fe939b207      488b45e8       rax = qword [var_18h]
│      │╎   0x556fe939b20b      4801d0         rax += rdx
│      │╎   0x556fe939b20e      0fb610         edx = byte [rax]
│      │╎   0x556fe939b211      8b45fc         eax = dword [var_4h]
│      │╎   0x556fe939b214      4898           cdq
│      │╎   0x556fe939b216      488d0dc33000.  rcx = rip + 0x30c3      ; 0x556fe939e2e0
│      │╎   0x556fe939b21d      0fb60408       eax = byte [rax + rcx]
│      │╎   0x556fe939b221      38c2           var = dl - al
│     ┌───< 0x556fe939b223      7407           if  (!var) goto loc_0x556fe939b22c
│     ││╎   0x556fe939b225      b800000000     eax = 0
│    ┌────< 0x556fe939b22a      eb0b           goto loc_0x556fe939b237
│    │└───> 0x556fe939b22c      8345fc01       dword [var_4h] += 1
│    │ │└─< 0x556fe939b230      ebc9           goto loc_0x556fe939b1fb
│    │ └──> 0x556fe939b232      b801000000     eax = 1
│    │      ; CODE XREF from check_password(char*) @ 0x556fe939b22a
│    └────> 0x556fe939b237      5d             rbp = pop  ()
└           0x556fe939b238      c3             re
[0x556fe939b1ec]> db 0x556fe939b1fb
[0x556fe939b1ec]> dc

Please Enter The Password: test
hit breakpoint at: 0x556fe939b1fb
[0x556fe939b1fb]> pdf
            ; CALL XREF from main @ 0x556fe939b1b4
┌ 77: sym.check_password_char_ (int64_t arg1);
│           ; var int64_t var_18h @ rbp-0x18
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           0x556fe939b1ec      55             push  (rbp)             ; check_password(char*)
│           0x556fe939b1ed      4889e5         rbp = rsp
│           0x556fe939b1f0      48897de8       qword [var_18h] = rdi   ; arg1
│           0x556fe939b1f4      c745fc000000.  dword [var_4h] = 0
│           ;-- rip:
│           ; CODE XREF from check_password(char*) @ 0x556fe939b230
│       ┌─> 0x556fe939b1fb b    837dfc0f       var = dword [var_4h] - 0xf
│      ┌──< 0x556fe939b1ff      7f31           if  (var > 0) goto loc_0x556fe939b232
│      │╎   0x556fe939b201      8b45fc         eax = dword [var_4h]
│      │╎   0x556fe939b204      4863d0         rdx = eax
│      │╎   0x556fe939b207      488b45e8       rax = qword [var_18h]
│      │╎   0x556fe939b20b      4801d0         rax += rdx
│      │╎   0x556fe939b20e      0fb610         edx = byte [rax]
│      │╎   0x556fe939b211      8b45fc         eax = dword [var_4h]
│      │╎   0x556fe939b214      4898           cdq
│      │╎   0x556fe939b216      488d0dc33000.  rcx = rip + 0x30c3      ; r9
│      │╎                                                              ; 0x556fe939e2e0 ; "isAAthisFunBBCCD"
│      │╎   0x556fe939b21d      0fb60408       eax = byte [rax + rcx]
│      │╎   0x556fe939b221      38c2           var = dl - al
│     ┌───< 0x556fe939b223      7407           if  (!var) goto loc_0x556fe939b22c
│     ││╎   0x556fe939b225      b800000000     eax = 0
│    ┌────< 0x556fe939b22a      eb0b           goto loc_0x556fe939b237
│    │└───> 0x556fe939b22c      8345fc01       dword [var_4h] += 1
│    │ │└─< 0x556fe939b230      ebc9           goto loc_0x556fe939b1fb
│    │ └──> 0x556fe939b232      b801000000     eax = 1
│    │      ; CODE XREF from check_password(char*) @ 0x556fe939b22a
│    └────> 0x556fe939b237      5d             rbp = pop  ()
└           0x556fe939b238      c3             re
[0x556fe939b1fb]> 
```

seems like `isAAthisFunBBCCD` is the key :D 

```
./crack2-by-D4RK_FL0W                                                                                                                                                                                                                                               ─╯

Please Enter The Password: isAAthisFunBBCCD


***Correct You Cracked It***
```
