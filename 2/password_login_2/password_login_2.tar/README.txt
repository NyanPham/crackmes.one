Password Login 2 by Loz

Tools used:
  Ghidra 9.1.2 disassembler
  objdump
  www.cplusplus.com (reference)
  "C++ Crash Course" by Josh Lospinoso (reference)

(Lengthy) Analsysis:
(Note, go to the summary section for a quick solution.)

The main function has command line arguments but never uses them. An
empty string is initialized and the getline function is called to populate it
with a user input value.

A password object is initialized. The password class contains a char and a
std::string data member that is seen in the constructor for the class. The char
data member is initialized to 0x42 (decimal 66) or ASCII letter B. The string
is initialized to the string literal "x_.1:.-8.4.p6-e.!-". What is not clear in
the constructor is that there is another data member of type int. This data
member will actually have a value assigned to it in the checkLength password
class method.

The user input value string then has the length method called on it to get the
length of the string. This value is then passed to the checkLength method in
the password class.

The checkLength method takes a int parameter and returns a boolean (integer 0
for false and any other value signifying true). A integer literal of 360 
(decimal) is converted to a std::string using the std::to_string function.
The returned string then has the at method called on it passing a 1 into the
method. The method pulls the character present at the integer (index) passed to
it. In this case, the character at index 1 is '6'. The string from the
std::to_string function call then uses the assignment operator member function
(=) to assign the character '6' to the string. The string now has the value
"6". The standard library (<cstdlib>) function atoi is used to convert the 
string, which has its c_str() method called on it to retrieve a c style
string, to an integer. This integer value is then added to 1. The sum, 7, is
then assigned to int data member of the password class mentioned above. This
honestly took me a few attempts at breaking down to finally catch this. This is
a really important portion of the program to figure out to solve. The int
data member is then compared to the length argument passed into the method.
If the values are equal a 1 is returned. A 0 is returned otherwise.

The return value from the checkLength method determines which branch the
program executes. If a 0 is returned, the program calls the password class
method wrongPassword and exits. If a 1 is returned, program execution
continues.

The input string is then copied to a new std::string. The copied string is then
passed to the checkPassword method.

The checkPassword method takes a std::string parameter and returns a boolean
value (0 for false, anything else true). A std::string is initialized as an
empty string. A loop is then entered with an index initialized to 0,
incremented by 1 with each iteration, and looping until the index is 1 less
than the string parameter's, passed into the checkPassword method, length
(this is via the string's length method). With each iteration, the char data
member from the password object is XOR'd with string parameter's character
at the iteration's index value in the string. This is done by passing the index
into the string's at method. The password object's char data member is 0x42.
The result of XOR'ing 0x42 with the character is the concatenated to the value
stored in the string initialized at the beginning of this method. This value
is initially an empty string.

Still in the checkPassword method, next comes the gotcha to me when analyzing
the program. I initially could not figure out what was happening. Eventually
I remembered the int data member of the password class having a memory offset
of 0 from the address of the password object. The assembly does some goofy
stuff from instruction 0x26b3 to 0x2719. Essentially all that really occurs
from a program execution standpoint, is that the integer data member of the
password class has its value retrieved and a c char array is made. I am still
a little uncertain on that last part but when I created a C++ source the
resulting binary is spot on, making me feel this is what is actually happening.
The string data member of the password class has its copy method called on it
passing in the c char array, the length data member of the password class, and
the integer literal 5. The method copies the characters from the string data 
member of the password class starting at sixth character (index 5) for 7
characters. The method returns the number of characters copied and that value
is stored in a variable. The variable is used as an index into the c char 
array to set the value at that index to 0, creating a null terminated string.
A new string is created with the value initialized to the c char array. This
string is then compared to the string generated from the XOR loop using the
string's == operator function. The result of the operator function is returned
as the value returned from the method.

If true is returned from checkPassword, the rightPassword method is called.
This completes the crackme. If false was returned, the wrongPassword method
is called.

Summary:

The string data member in the password class is "x_.1:.-8.4.p6-e.!-".
This is used as a base to generate the key.
The correct solution only uses 7 characters of the string, starting at index 5
(the sixth character).
From that, we now have the string ".-8.4.p".
The password class also contains a char data member initialized to 0x42 ('B').
A cool feature of the XOR function is that XOR'ing a value twice with a
constant gets a user back to the original value. Using this, one needs to XOR
the string ".-8.4.p" with the constant 0x42 (the char data member) to get the
correct user input "lozlvl2".

A simple "keygen" file, solution.c, is included. An attempt at recreating the
source code is included in the file password.cpp.

$ gcc -Wall -o solution solution.c
$ ./solution
$ ./main < input

- dev0470

