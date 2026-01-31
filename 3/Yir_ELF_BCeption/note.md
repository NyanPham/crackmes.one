# ANALYSIS

We use scanf to get a dword num from user.
We break this num into 4 bytes, a, b, c, and d, where a stores the LSB and d stores the MSB of the num.

we have a struct, temp name is buf1

struct VM
{
    char ram[0x114];
    uint32_t sp;
    uint32_t ip;
}


x = a, y = 4, z = 4

buf2 is already defined in the .data section.
ret_val = f_check(buf1, buf2, 0x55)

if  ret_val == 4:
    succeed
else:
    fail



--- 

Here is the flow: of the VM
The f_check function recieves a VM, and a buf of instructions, and length of the buf as well.
The VM has 3 fields: ram, sp, and ip

Each instruction takes up 2 bytes, except the load_reg instruction that takes up 3 bytes.
Each instruction has the first byte as an `opcode`, the second byte is broken down into high and low nibbles, acting as the registers of the VM (in ram).

Each nibble is 4-bit wide, so the largest index of registers could be 0xF (15), but actually we have only 14 registers. I don't know why. 
So ram[0:15] elements are registers to store data. ram[15] is the Equal Flag, ram[16] is the Above Flag, and ram[17] is the Below flag. That leaves the ram[18] is the beginning of the usable free stack memory of the VM.

That's why we see when we need to access the stack memory of the VM with vm->sp, we always see `vm->sp+18`. 

Now for the case of load_reg instruction which has 3 bytes, it's when opcode is 1. In this case, we access the last byte with `vm->ip+2`, and deliberately adds 1 to the ip to move on.

Opcode 2: mov reg, reg
Opcode 3 -> 9: +, -, *, .etc
Opcode 10: reg == 0?
Opcode 11-> 12: shift 
Opcode 13: jnz
Opcode 14: jz
Opcode 15: ja
Opcode 16: jna
Opcode 17: jb
Opcode 18: jnb
Opcode 19: push reg to stk
Opcode 20: pop stk to reg
Opcode 21: cmp reg, ref -> affect flags at ram[15:18]
Opcode 22: stops the VM, return the value at ram[reg]

User's input, which is already splitted into 4 bytes, are stored index 18 of ram, which is the right on top of the stack


```
struct VM
{
    char ram[0x114];
    uint32_t sp;
    uint32_t ip;
}

f_get_num():
    get a dword from user

f_split_num():
    split a dword into an array of 4 one-byte num. little endian, so the least siginificant byte is the first num and so on

f_get_high_nib(n):
    return (n >> 4) & 0xF 

f_get_low_nib(n):
    return n & 0xF

f_check(vm, instrs, n):
    buf1.pos = 0

    while (vm.ip <= n):
        a = instrs[vm.ip]
        b = instrs[vm.ip+1]
        
        if (a == 1): // load reg
            c = instrs[vm.ip+2]
            vm.ram[b] = c
            vm.ip += 1
        elif (a == 2):
            t1 = f_get_high_nib(n)
            t2 = f_get_low_nib(n)
            vm.ram[t1] = vm.ram[t2]
        elif (a == 3):
            b_low = f_get_low_nib(n)
            b_high = f_get_high_nib(n)
            vm.ram[b_high] += vm.ram[b_low]
        elif (a == 4):
            b_low = ...
            b_high = ...
            vm.ram[b_high] -= vm.ram[b_low]
        elif (a == 5):
            b_low = ...
            b_high = ...
            vm.ram[b_high] *= vm.ram[b_low]
        elif (a == 6):
            b_low = ...
            b_high = ...
            vm.ram[b_high] /= vm.ram[b_low]
        elif (a == 7):
            vm.ram[b_high] ^= vm.ram[b_low]
        elif (a == 8):
            vm.ram[b_high] |= vm.ram[b_low]
        elif (a == 9):
            vm.ram[b_high] &= vm.ram[b_low]
        elif (a == 10):
            vm.ram[b_high] = vm.ram[b_low] == 0
        elif (a == 11):
            vm.ram[b_high] <<= vm.ram[b_low]
        elif (a == 12):
            vm.ram[b_high] >>= vm.ram[b_low](signed)
        elif (a == 13):
            if (vm.ram[15] != 0):
                vm.ip = b - 2
        elif (a == 14):
            if (vm.ram[15] == 0):
                vm.ip = b -2
        elif (a == 15):
            if (vm.ram[16] != 0):
                vm.ip = b - 2
        elif (a == 16):
            if (vm.ram[16] == 0):
                vm.ip = b - 2
        elif (a == 17):
            if (vm.ram[17] != 0):
                vm.ip = b - 2
        elif (a == 18):
            if (vm.ram[17] == 0):
                vm.ip = b - 2
        elif (a == 19):
            vm.ram[vm.sp+18] = vm.ram[b]
            vm.sp += 1
        elif (a == 20):
            vm.ram[b] = vm.ram[vm.sp+18]
            vm.sp -= 1
        elif (a == 21):
            b_high = ...
            b_low = ...
            d = vm.ram[b_high]
            e = vm.ram[b_low]

            for (x = 0; x <= 2; x++):
                vm.ram[x+15] = 0
            
            if (d == e):
                vm.ram[15] = 1
            elif (d > e):
                vm.ram[16] = 1 
            elif (d < e):
                vm.ram[17] = 1
        elif (a == 22):
            return vm.ram[b]

        vm.ip += 2


    return -1
```
