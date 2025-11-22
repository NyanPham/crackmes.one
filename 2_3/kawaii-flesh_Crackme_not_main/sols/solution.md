# Disassembly

First we disassemble the program. We can see that it compares first argument (which is the binary itself, to an input string):

```c
  char local_68 [88];
  printf("Enter key: ");
  scanf("%79s",local_68);
  iVar1 = strcmp(local_68,*argv);
```

and then it reads and compares a bunch of numbers:

```c
    if ((((local_74 == 1) && (scanf("%d",&local_74), local_74 == 7)) &&
        (scanf("%d",&local_74), local_74 == 8)) &&
       (scanf("%d",&local_74), local_74 == 5))
```

So to get correct answer we input the name of the binary "./CNM" and the passkey "1785".

This creates the `CNP.7z` file.

# Xoring

Unpacking reveals `key` and `XOR_REV(QWER=RIFF)`.

Using this small program in [Nim](https://nim-lang.org) we perform bitwise xor on two files.
Also, the first 4 bytes in resulting file are `QWER` so we exchange them for `RIFF`.

```nim
import bitops

let
  f1 = readFile "key"
  f2 = readFile "XOR_REV(QWER=RIFF)"

var f3 = newString(f1.len)

f3[0..3] = "RIFF"

for i in 4..f1.high:
  f3[i] = chr bitxor(f2[i].ord, f1[i].ord)

writeFile "output.riff", f3
```

This results in `output.riff` file being created.

# Morse

Opening `output.riff` in audioplayer reveals that its morse code audio.
Using audacity, we reverse the audio and transcript it to morse code.

`..-. .-.. .- --. ---... .---- ....- .---- ...-- ..... -.... --... ---.. ----- ----.`

which translates to `FLAG:1413567809` which is a flag we're looking for.
