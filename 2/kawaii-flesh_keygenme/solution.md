# Solution for keygenme 
This was solved by disassembly
## Disassembled code
disassembled main function
```c
int main(int argc,char **argv) {
  char cVar1;
  int iVar2;
  ulong uVar3;
  size_t sVar4;
  
  if (argc == 3) {
    uVar3 = acum_input_atoi(argv[1]);
    cVar1 = *argv[1];
    sVar4 = strlen(*argv);
    iVar2 = atoi(argv[2]);
    if ((uVar3 ^ cVar1 * 3) << (sVar4 & 0x1f) == iVar2) {
      puts("Good job!");
    }
    else {
      puts("Wrong key!");
    }
  }
  else {
    puts("keygenme [name] [key]");
  }
  return 0;
}
```

Disassembled acum_input_atoi
```c
ulong acum_input_atoi(char *pcParm1)

{
  size_t sVar1;
  uint return_val;
  int idx;
  
  return_val = 0;
  idx = 0;
  while( true ) {
    sVar1 = strlen(pcParm1);
    if (sVar1 <= idx) break;
    return_val = return_val + pcParm1[idx];
    idx = idx + 1;
  }
  return return_val;
}
```

From here it is clear that cVar1 is the decimal value of the first char of the username
sVar4 is the length of the abs_path to the keygenme executable
iVar2 is the number input as the passphrase
uVar3 is the cummulated sum of the decimal value of the characters in the username

Form this it is simply a matter of making a keygen that takes in the abs path to the keygenme and the username, 

then do the calculation
```c 
(uVar3 ^ cVar1 * 3) << (sVar4 & 0x1f)
```

## Keygen
```python
# Keygen for crackme

import argparse
import os

parser = argparse.ArgumentParser(description="Keygen for the keygenme file.")
parser.add_argument("-n", "--name", help="Username to be used with the keygenme application")
parser.add_argument("-p", "--path_to_keygenme", nargs="?", help="if the keygenme is not placed in the same directory as this keygen, provide the full system path to the applications")

args=parser.parse_args()

user_name=args.name
path_to_keygenme=""
if not args.path_to_keygenme:
    if os.path.isfile(os.getcwd()+"/keygenme"):
        path_to_keygenme=os.getcwd()+"/keygenme"
else:
    path_to_keygenme=args.path_to_keygenme

username_acum_value=0
for char in user_name:
    username_acum_value=username_acum_value+ord(char)

first_char = ord(user_name[0])
path_length=len(path_to_keygenme)

pwd=(username_acum_value^(first_char*3))<<(path_length&0x1f)

print("Password for username: " + user_name + "\nWith keygenme at: " + path_to_keygenme + "\nis: " + str(pwd))
print("To validata execute:")
print(path_to_keygenme + " " + user_name + " " + str(pwd))
    
```
