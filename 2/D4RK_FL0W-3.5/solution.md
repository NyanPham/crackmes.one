# D4RKFL0W's D4RK_FL0W-3.5

## Deetz
Author: D4RKFL0W
Language: C/C++
Upload: 11:02 AM 05/19/2019
Arch: x86-64
Description: A few extra functions this time plus minimal uses of classes
Link: https://crackmes.one/crackme/5ce137b933c5d4419da55ac2

## RE

Takin' a peek at main we can see that the `Password` class is instantiated and two methods are called from it: `get_input` and `check_passcode`. We want the outcome of that function to be `\0`. Let's checkem' out!

```c++
int main(void) {
  
  Password::get_input((Password *)p);
  char cVar1 = Password::check_passcode((Password *)p);

  if (cVar1 != '\0') {
    std::operator<<((basic_ostream *)std::cout,"\nWell done");
  }

  std::operator<<((basic_ostream *)std::cout,"\n\nSORRY MAYBE NEXT TIME!!");
  return 0;
}
```

### `get_input`
```c++
void __thiscall Password::get_input(Password *this) {
	std::operator<<((basic_ostream *)std::cout,"\nPlease Enter Four Digits Seperately: ");
	std::cin,&this->digit1;
	std::operator<<((basic_ostream *)std::cout,"\nSecond Digit: ");
	std::cin,&this->digit2;
	std::operator<<((basic_ostream *)std::cout,"\nThird Digit: ");
	std::cin,&this->digit3;
	std::operator<<((basic_ostream *)std::cout,"\nFourth Digit: ");
	std::cin,&this->digit4;
	std::operator<<((basic_ostream *)std::cout,"\n\n");
	return;
}
```

### `check_passcode`

This is the most important function to us as it's what we need to "crack". We can see that of the 8 members in the password struct this is checking the first 4 against the last 4. But how are those first 4 members being populated? Let's look at the definition for the `Password` class. 
```c++
undefined8 __thiscall Password::check_passcode(Password *this) {
  if (this->digit1 == this->answer1) {
    if (this->digit3 == this->answer3) {
      if (this->digit2 == this->answer2) {
        if (this->digit4 == this->answer4) {
          uVar2 = 1;
        }
        else { uVar2 = 0; }
      }
      else { uVar2 = 0; }
    }
    else { uVar2 = 0; }
  }
  else { uVar2 = 0; }
  return uVar2;
}
```

### `Password`

Ok great! We can see that when this class is instantiated 4 functions are called to populate the first 4 members of a password. Opening these functions up, we can see that they all return the result of some basic operation on the parameter. Let's throw those into a lil' python script and we should have our answer!

```c++
void __thiscall Password::Password(Password *this) { 
  this->answer1 = get_num1(this, 0x28, 0x7ebd);
  this->answer2 = get_num2(this, 1, 4);
  this->answer3 = get_num3(this, 0x46);
  this->answer4 = get_num4(this, 0x8a7d, 0x345);
  return;
}
```

## Solution Script

```python
def get_num1(param_1: int, param_2: int) -> int:
	return (param_2 + param_1) % 9

def get_num2(param_1: int, param_2: int) -> int:
	return ((param_2 + param_1) * 2 + 1) % 9

def get_num3(param_2: int) -> int:
	return param_2 % 9

def get_num4(param_1: int, param_2: int) -> int:
	return (param_1 + 10 + param_2) % 9

print(get_num1(0x28,0x7ebd))
print(get_num2(1,4))
print(get_num3(0x46))
print(get_num4(0x8a7d,0x345))
```

Running should give us our answer!

```bash
➜  D4RK_FL0W-3.5 python3 solve.py
4
2
7
3
```