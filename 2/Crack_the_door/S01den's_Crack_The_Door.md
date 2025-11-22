# S01den's Crack The Door
## Solution

Interesting crackme. The program starts by initializing two 12 bytes-long value on the stack (at 0x400d16). Let's call it a and b:
- a = 0x54484550495241544549535a
- b = 0x3f2a2d2f353937243d232640

Thoses values will later be used to verify the password.

Then, the program print a cool ASCII-Image of an keyboard and a LCD screen, and ask for an username.
It checks if the username is 12 char long (including \n). If the username has the good length. It asks for the password (which must be 12 bytes long too)

After that, the check-computation is pretty clear.The program check the username/password 2 bytes at a time.
If the computation is correct, it increments a counter by 2.
At the end, if the counter equals 12, it prints the success message.

Here's the verification algorithm:

```
tmp1 = ((*(BYTE)(&a + i) + 50) ^ username[i]) % 100 + 65
tmp2 = *(BYTE)(&b + (9*i + 5) % 12)

if (tmp1 == passwd[i] && tmp2 == passwd[i + 1]){
    counter+=2
}
```

So we can implement the keygen:

```python3
a = [0x54, 0x48, 0x45, 0x50, 0x49, 0x52,0x41, 0x54, 0x45, 0x49, 0x53, 0x5a]
b = [0x3f, 0x2a, 0x2d, 0x2f, 0x35, 0x39, 0x37,0x24, 0x3d, 0x23, 0x26, 0x40]
usr = input("Username: ")
pwd = []
if len(usr) != 11:
    print("len(usr) must be 12")
else:
    for i in range(0, 6):
        pwd.append(chr(((a[2*i] + 50)^ ord(usr[2*i]))%100 + 65))
        pwd.append(chr(b[(9*2*i+5)%12]))
    print("Password:", ''.join(pwd))
```

Thanks S01den !

