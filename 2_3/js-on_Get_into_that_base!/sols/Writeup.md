# Get into that base made by js-on
[You can find it here](https://crackmes.one/crackme/5ed3cd9a33c5d449d91ae6b1)

After starting crackme a password prompt appears:

```bash
./guessme
Your guess: pass
S0RRY!
```

If an incorrect password is entered, crackme politely apologizes to us.
So we have to find a correct password.

First thing first I opened an ELF file in Ghidra and change names of local variables.

```cpp
ulong main(void)

{
  int mcs_digit_sum;
  basic_ostream *this;
  long in_FS_OFFSET;
  bool password_is_correct;
  int user_input;
  int password;
  undefined4 local_74;
  long seconds;
  long microseconds;
  long miliseconds;
  timeval timeval_stuct;
  basic_string_char_std__char_traits_char__std__allocator_char__ string [40];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  allocator();
  basic_string((char *)string,(allocator *)&DAT_00102009);
  _allocator((allocator_char_ *)&timeval_stuct);

  gettimeofday(&timeval_stuct,(__timezone_ptr_t)0x0);
  
  seconds = timeval_stuct.tv_sec;
  microseconds = timeval_stuct.tv_usec;
  miliseconds = (long)((double)timeval_stuct.tv_usec / 1000.00000000 + (double)(timeval_stuct.tv_sec * 1000));
  
  mcs_digit_sum = digit_sum(timeval_stuct.tv_usec);
  password = (int)(miliseconds % (mcs_digit_sum * microseconds));
  local_74 = 0x42;
  
  operator___std__char_traits_char__((basic_ostream *)cout,"Your guess: ");
  operator__((basic_istream_char_std__char_traits_char__ *)cin,&user_input);
  password_is_correct = password != user_input;

  if (password_is_correct) {
    this = operator___std__char_traits_char__((basic_ostream *)cout,"S0RRY!");
    operator__((basic_ostream_char_std__char_traits_char__ *)this,endl_char_std__char_traits_char__);
  }
  else {
    this = operator___std__char_traits_char__((basic_ostream *)cout,"R");
    this = operator___std__char_traits_char__(this,"z");
    this = operator___std__char_traits_char__(this,'A');
    this = operator___std__char_traits_char__(this,"w");
    this = operator___std__char_traits_char__(this,"R");
    this = operator___std__char_traits_char__(this,'C');
    this = operator___std__char_traits_char__(this,(char)local_74);
    operator___char_std__char_traits_char__std__allocator_char__(this,(basic_string *)string);
    this = operator___std__char_traits_char__((basic_ostream *)cout,"IhC");
    this = operator___std__char_traits_char__(this,"g");
    operator__((basic_ostream_char_std__char_traits_char__ *)this,endl_char_std__char_traits_char__)
    ;
  }
  _basic_string(string);
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return (ulong)password_is_correct;
}
```

In order to make it more readable I rewrote the whole crackme mainly for presentation purposes.

```cpp
int main() {
    timeval current_time;
    gettimeofday(&current_time, nullptr);

    ulong seconds = current_time.tv_sec;
    ulong microseconds = current_time.tv_usec;
    ulong miliseconds = seconds / 1000.0 + microseconds * 1000;
    uint microseconds_digit_sum = digit_sum(microseconds);

    uint password = miliseconds % (microseconds_digit_sum * microseconds);
    uint user_input;
    
    std::cout << "Guess: ";
    std::cin >> user_input;

    bool password_is_correct = (password != user_input);

    if (password_is_correct) {
        std::cout << "Sorry!" << std::endl;
    } else {
        std::cout << "RzAwrCInCg" << std::endl;
    }

    return password_is_correct;
}
```

The password is based on the time which is returned by gettimeofday function.
From linux man I got additional info about gettimeofday.

Function prototypes:
```cpp
int gettimeofday(struct timeval *tv, struct timezone *tz);
int settimeofday(const struct timeval *tv, const struct timezone *tz);
```

The function takes two arguments. The first one stores information about time and the second about time zone.
In this example only first argument is set, the second one is nullptr.

timeval type:
```cpp
struct timeval {
    time_t      tv_sec;     /* seconds */
    suseconds_t tv_usec;    /* microseconds */
};
```

Time is stored in the current_time variable. Seconds (current_time.tv_sec) and microseconds (current_time.tv_usec) are copied to relevant variables.
After that seconds and microseconds are combined into miliseconds. To do that we multiply seconds by 1000 and then add a number constructed from the first 3 digits of microseconds.

Example:
```plain
seconds: 1594730719
microseconds: 940827
miliseconds: 1594730719 * 1000 + 940827/1000 = 1594730719000 + 940 = 1594730719940
```

Miliseconds are unsigned long type so fractional part is rejected in final result.

Next program calculates microseconds digits sum. It's achieved by calling digit_sum funtion (orginally named as cross_sum).

```cpp
ulong cross_sum(long microseconds)

{
  ulong p1;
  ulong p2;
  ulong p3;
  double ln_microseconds;
  double ln_10;
  uint sum;
  int exponent;
  
  log<long>(microseconds);
  log<int>(10);
  sum = 0;
  exponent = 0;
  while (exponent < (int)(ln_microseconds / ln_10 + 1.00000000)) {
    p1 = power(10,exponent);
    p2 = power(10,exponent + 1);
    p3 = power(10,exponent);
    sum = sum + (int)(((microseconds - microseconds % (long)(int)p1) % (long)(int)p2) /
                     (long)(int)p3);
    exponent = exponent + 1;
  }
  return (ulong)sum;
}
```

While loop proceed until exponent is lower than the number of all digits in microseconds.

Example:
```
microseconds: 940827
exponent: 0

while (exponent < 6) {
    ...
    ...
}
```

Function add all digits from microseconds without the last one. When I tried to calculate the sum value, my result did not match the result given by the program.
I was suprised and rerun program in debugger in order to check what is going on. My second suprise came out when I saw that power(10, 0) = 10. I checked assembly code of power function and
everything became clear.

```nasm
┌ 52: sym.p_int__int (int64_t arg1, int64_t arg2);
│           ; var int64_t exponent @ rbp-0x18
│           ; var int64_t base @ rbp-0x14
│           ; var int64_t result @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           ; arg int64_t arg2 @ rsi
│           push rbp                    
│           mov rbp, rsp
│           mov dword [base], edi       ; arg1
│           mov dword [exponent], esi   ; arg2
│           mov eax, dword [base]
│           mov dword [result], eax
│           mov dword [var_4h], 1
│           
│       ┌─> mov eax, dword [var_4h]
│       ╎   cmp eax, dword [exponent]   ; check if value stored in eax is greater than or equal to exponent
│      ┌──< jge _end                    
│      │╎   mov eax, dword [result]
│      │╎   imul eax, dword [base]
│      │╎   mov dword [result], eax
│      │╎   add dword [var_4h], 1
│      │└─< jmp 0x5619c19b3230
│      └──> _end:
|           mov eax, dword [result]
│           pop rbp
└           ret
```

For power(10, 0) assembly code looks like that:
``` nasm
┌ 52: sym.p_int__int (int64_t arg1, int64_t arg2);
│           ; var int64_t exponent @ rbp-0x18
│           ; var int64_t base @ rbp-0x14
│           ; var int64_t result @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           ; arg int64_t arg2 @ rsi
│           push rbp                    
│           mov rbp, rsp
│           mov dword [base], edi       ; 10
│           mov dword [exponent], esi   ; 0
│           mov eax, dword [base]       ; eax = 10
│           mov dword [result], eax     ; result = 10
│           mov dword [var_4h], 1       ; var_4h = 1
│           
│       ┌─> mov eax, dword [var_4h]     ; eax = 1
│       ╎   cmp eax, dword [exponent]   ; eax > exponent => 1 > 0
│      ┌──< jge _end                    ; So we make a jump
│      │╎   mov eax, dword [result]
│      │╎   imul eax, dword [base]
│      │╎   mov dword [result], eax
│      │╎   add dword [var_4h], 1
│      │└─< jmp 0x5619c19b3230
│      └──> _end:
|           mov eax, dword [result]     ; eax = 10
│           pop rbp
└           ret
```

And this is why power(10, 0) = 10. Here is a C code of power function obtained from Ghidra:

```cpp
ulong power(int base,int exponent)

{
  uint pow;
  int i;
  
  i = 1;
  pow = base;
  while (i < exponent) {
    pow = pow * base;
    i = i + 1;
  }
  return (ulong)pow;
}
```

When the cross_sum job is done, the final password is calculated by using this formula:

```plain
    password = miliseconds % (microseconds_digit_sum * microseconds);
```

Here is whole rewroted code. I added some debug information in presentation purposes.
Code should be compiled on linux with compiler which supports C++17.

```cpp
#include <iostream>
#include <sys/time.h>
#include <cmath>

constexpr bool debug_flag = true;

uint digit_sum(long number) {
    uint sum = 0;
    uint debug_sum = 0;

    int exponent = 0;

    while (exponent < int(log(number) / log(10) + 1)) {

        ulong p1 = (exponent == 0) ? 10 : pow(10, exponent);
        ulong p2 = pow(10, exponent + 1);
        ulong p3 = (exponent == 0) ? 10 : pow(10, exponent);
        
        sum += int(((number - number % p1) % p2) / p3);
        
        if constexpr (debug_flag) {
            debug_sum = number % p1;
            std::cout << "-----------------------" << std::endl;
            std::cout << "p1: " << p1 << " p2: " << p2 << " p3: " << p3 << std::endl;
            std::cout << number << " % " << p1 << " = " << debug_sum << std::endl;
            debug_sum = number - debug_sum;
            std::cout << number << " - " << (number % 10) << " = " << debug_sum << std::endl;
            std::cout << debug_sum << " % " << p2 << " = " << (debug_sum %= p2) << std::endl;
            std::cout << debug_sum << " / " << p3 << " = " << (debug_sum /= p3) << std::endl;
            std::cout << "sum: " << sum << std::endl;
        }

        exponent++;
    }

    return sum;
}

int main() {
    timeval current_time;
    gettimeofday(&current_time, nullptr);

    ulong seconds = current_time.tv_sec;
    ulong microseconds = current_time.tv_usec;
    ulong miliseconds = microseconds / 1000.0 + seconds * 1000;
    uint microseconds_digit_sum = digit_sum(current_time.tv_usec);

    uint password = miliseconds % (microseconds_digit_sum * microseconds);
    uint user_input;
    
    if constexpr (debug_flag) {
        std::cout << "-----------------------" << std::endl;
        std::cout << "seconds: " << seconds << std::endl;
        std::cout << "microseconds: " << microseconds << std::endl;
        std::cout << "miliseconds: " << miliseconds << std::endl;
        std::cout << "digit_sum: " << microseconds_digit_sum << std::endl;
        std::cout << "password: " << password << std::endl; 
        std::cout << "-----------------------" << std::endl;
    }

    std::cout << "Guess: ";
    std::cin >> user_input;
    
    bool password_is_correct = (password != user_input);

    if (password_is_correct) {
        std::cout << "Sorry!" << std::endl;
    } else {
        std::cout << "RzAwrCInCg" << std::endl;
    }

    return password_is_correct;
}
```

GDB script:
```palin
b *main+210

set pagination off
set prompt

r

echo seconds: 
x/dg $rbp-0x68
echo microseconds: 
x/dg $rbp-0x60
echo miliseconds: 
x/dg $rbp-0x58
echo password:
x/dw $rbp-0x70
echo Copy password and continue program execution (enter c or continue)\n
```

Used tools:
- Ghidra
- Radare2
- GDB