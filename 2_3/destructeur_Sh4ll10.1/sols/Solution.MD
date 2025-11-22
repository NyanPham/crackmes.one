First observation -
I executed the ELF, and it is a simple prog which gets input from the user,
and checks whether the input was correct or no.

First step -
I tried typing a random password, and checked what the output will be - as expected
I didn't guess it right, so output was "Bad Password"

Second step -
I opened the program with cutter, and watched the graph of the main function.
--------------------------------------------------------------------------------
The actual solution -
so I went through the disassembly and saw that there is a var which is named -
"falsePassword[abi:cxx11]", and it compares with our input, which is stored in
"0x602340".
Actually, the false password is stored in the executable, and it is -
"1d47faf54f84dc393a4a015a8f190e36".
This is not the password, because if the compares actually works, it jumps to
"Bad Password" Path and terminates.
So, I kept reading through the code, and saw that the password's length is
actually bigger than 3, because as before it calls str length and compares it
3(whether its smaller or equals).
So, I have another hint.
I kept reading, and saw an interesing pattern.

  mov esi, 0
  mov edi, 0x602340
  call 0x400f20
  movzx ebx, byte [rax]
  mov esi, 0
  mov edi, 0x602320
  call 0x400f20
  movzx eax, byte [rax]
  cmp bl, al
  jne 0x4011c6

so, this is actually checks whether the input[0] == falsePassword[5]
and it keeps going like that until input[4].
if we are right we keep going, else we go to the "Bad Password" path.
So , these are the conditions -
  input[0] == falsePassword[0]
  input[1] == falsePassword[5]
  input[2] == falsePassword[8]
  input[3] == falsePassword[9]
So, we take the chars, and we get the pass - "1a4f" :)
but.. It's not the pass! cause it is written that if theres no output, then the
elf isn't validated, so! we need to check for more stuff!
So, there's another suspicios func, which is suspicios due to the fact that its
as long as main, and its calling main, and uses our input, which we got from
main.
So after reading the func a bit, I found these lines -
  mov esi, 4
  mov edi, 0x602340
  call 0x400f20
  mov esi, 1
  mov edi, 0x602340
  call 0x400f20
  movzx eax, byte [rax]
  cmp bl, al
which mean that out input[4] = input[1] -> 'a'
then, similiar thing -
  mov esi, 5
  mov edi, 0x602340
  call 0x400f20
  ..
  ..
but this time
  cmp al, 0x40
so, input[5] = chr(0x40) = '@'
and then some stuff that didn't include the input, and we didnt have any control
on. so - The pass is - "1a4fa@"
and it gives the correct output - "Well played! This is the only valid flag."
and we are done :)
