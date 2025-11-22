This is a simple Linux crackme. Inside the main() function, at 0x4010be, it first checks if the user input is equal to a constant string. This constant string is initialized to "1d47faf54f84dc393a4a015a8f190e36" at 0x401548. However, as the name of the constant string (falsePassword) indicates, this check does not give you the correct answer. 

Moving forward within the main(), the code checks the following consitions:

1. strlen(user_input) > 3
2. user_input[0] == falsePassword[0]
3. user_input[1] == falsePassword[5]
4. user_input[2] == falsePassword[8]
5. user_input[3] == falsePassword[9]

When all of the 5 criteria are met, eax will be set to 1 at 0x4011bf and the code will load "Good Password" at 0x4011d3. main() will return 1 in this case. 

However, this does not solve the crackme yet. After the main returns, we find the check continues in function _static_initialization_and_destruction (0x401281). The loop at 0x4012ba is irrelevant and can be ignored. 

After analyzing the code, we find there are 3 further criteria:

6. main() must return 1
7. user_input[4] == user_input[1]
8. user_input[5] == '@'

So the correct password is "1a4fa@". And we get the flag "Well played! This is the only valid flag." as shown below:

$ ./Sh4ll10.1.bin 
The goal is to print the good boy. Good luck
If there is no output printed, then you didn't validate the crackme
1a4fa@                                 
Well played! This is the only valid flag.

It turns out the flag is actually the result of xor-ing the string at rbp-0xa0 with 0x78. So it is also possible to get the flag without deducing the correct password. 

Author: Xusheng Li