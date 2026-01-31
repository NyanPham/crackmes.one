import sys

class VMState:
    def __init__(self):
        # struct buf_w_pos: char bur[0x114]
        # We simulate this as a list of integers (0-255)
        self.memory = [0] * 0x114 
        # R0E (Index 14) is the Success Counter (0-4)
        # R0F (Index 15) is the Equal Flag (ZF)
        # R10 (Index 16) is the Greater Flag (CF)
        # R11 (Index 17) is the Less Flag (SF)
        
        # Renamed from 'idx' to 'stack_ptr' for clarity. This is the index 
        # pointer (r8 in the solution analysis) used by PUSH/POP operations.
        self.stack_ptr = 0  
        
        self.pos = 0  # uint32_t pos (Program Counter/EIP)

class VM:
    def __init__(self):
        self.state = VMState()

    def get_high_nib(self, n):
        """Returns the high 4 bits of a byte."""
        return (n >> 4) & 0xF

    def get_low_nib(self, n):
        """Returns the low 4 bits of a byte."""
        return n & 0xF

    def load_input(self, dword_val):
        """
        Simulates f_split_num.
        Splits a 32-bit int into memory locations 1-4 (Little Endian).
        
        The solution implies:
        [1] = LSB+1 (Byte 1)
        [2] = LSB+2 (Byte 2)
        [3] = LSB+3 (Byte 3)
        [4] = MSB (Byte 4)
        """
        self.state.memory[1] = dword_val & 0xFF        # LSB
        self.state.memory[2] = (dword_val >> 8) & 0xFF
        self.state.memory[3] = (dword_val >> 16) & 0xFF
        self.state.memory[4] = (dword_val >> 24) & 0xFF # MSB

    def check(self, bytecode):
        """
        The main interpreter loop (f_check).
        bytecode: A list of integers or bytes representing the instruction stream 'buf'.
        """
        # Reset PC
        self.state.pos = 0
        n = len(bytecode)

        # Loop until PC exceeds bytecode length
        while self.state.pos < n:
            # Safe access to bytecode
            try:
                a = bytecode[self.state.pos]      # Opcode
                b = bytecode[self.state.pos + 1]  # Operand 1 (always a byte)
            except IndexError:
                break

            # --- Instruction Dispatch ---

            if a == 1:
                # Load Immediate: MEM[b] = Immediate Value (3 byte instruction)
                if self.state.pos + 2 < n:
                    c = bytecode[self.state.pos + 2]
                    self.state.memory[b] = c
                    # The instruction is 3 bytes long. PC increment should advance 3 total.
                    self.state.pos += 1 

            elif a == 2:
                # Move: MEM[HighNib] = MEM[LowNib]
                t1 = self.get_high_nib(b)
                t2 = self.get_low_nib(b)
                self.state.memory[t1] = self.state.memory[t2]

            elif a == 3:
                # Add
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                res = self.state.memory[b_high] + self.state.memory[b_low]
                self.state.memory[b_high] = res & 0xFF

            elif a == 4:
                # Subtract
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                res = self.state.memory[b_high] - self.state.memory[b_low]
                self.state.memory[b_high] = res & 0xFF

            elif a == 5:
                # Multiply
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                res = self.state.memory[b_high] * self.state.memory[b_low]
                self.state.memory[b_high] = res & 0xFF

            elif a == 6:
                # Divide (Integer)
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                divisor = self.state.memory[b_low]
                if divisor != 0:
                    res = int(self.state.memory[b_high] / divisor)
                    self.state.memory[b_high] = res & 0xFF
                else:
                    self.state.memory[b_high] = 0 # Handle div by zero if necessary

            elif a == 7:
                # XOR
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                self.state.memory[b_high] ^= self.state.memory[b_low]

            elif a == 8:
                # OR
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                self.state.memory[b_high] |= self.state.memory[b_low]

            elif a == 9:
                # AND
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                self.state.memory[b_high] &= self.state.memory[b_low]

            elif a == 10:
                # Logic NOT / Is Zero
                # Sets destination to 1 if source is 0, else 0
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                val = self.state.memory[b_low]
                self.state.memory[b_high] = 1 if val == 0 else 0

            elif a == 11:
                # Left Shift
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                shift_amt = self.state.memory[b_low]
                res = self.state.memory[b_high] << shift_amt
                self.state.memory[b_high] = res & 0xFF

            elif a == 12:
                # Right Shift (Signed)
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                shift_amt = self.state.memory[b_low]
                val = self.state.memory[b_high]
                
                # Convert to signed 8-bit for the operation
                if val > 127:
                    val -= 256
                
                res = val >> shift_amt
                self.state.memory[b_high] = res & 0xFF

            # --- Jumps ---
            # Note: Logic is 'pos = b - 2'. Since loop does 'pos += 2' at end,
            # effective new pos is 'b'.
            
            elif a == 13: # JNE (Jump if reg 15 != 0) - Original logic
                if self.state.memory[15] != 0:
                    self.state.pos = b - 2

            # Opcode 14 (0xE) is JNZ on the Equal Flag (reg 15).
            # Since reg 15 is 1 when Equal, this acts as a JE (Jump if Equal).
            elif a == 14: # JE (Jump if reg 15 != 0) - Corrected for crackme
                if self.state.memory[15] != 0: 
                    self.state.pos = b - 2

            elif a == 15: # JG (Jump if reg 16 != 0)
                if self.state.memory[16] != 0:
                    self.state.pos = b - 2

            elif a == 16: # JLE (Jump if reg 16 == 0)
                if self.state.memory[16] == 0:
                    self.state.pos = b - 2

            elif a == 17: # JL (Jump if reg 17 != 0)
                if self.state.memory[17] != 0:
                    self.state.pos = b - 2
            
            elif a == 18: # JGE (Jump if reg 17 == 0)
                if self.state.memory[17] == 0:
                    self.state.pos = b - 2

            # --- Stack Operations ---
            
            elif a == 19:
                # Push: Stack[stack_ptr + 18] = MEM[b], stack_ptr++
                stack_pos = self.state.stack_ptr + 18
                if stack_pos < len(self.state.memory):
                    self.state.memory[stack_pos] = self.state.memory[b]
                    self.state.stack_ptr += 1

            elif a == 20:
                # Pop: MEM[b] = Stack[stack_ptr+18], stack_ptr--
                if self.state.stack_ptr > 0:
                    self.state.stack_ptr -= 1
                    stack_pos = self.state.stack_ptr + 18
                    self.state.memory[b] = self.state.memory[stack_pos]
                
            # --- Compare ---

            elif a == 21:
                b_low = self.get_low_nib(b)
                b_high = self.get_high_nib(b)
                d = self.state.memory[b_high]
                e = self.state.memory[b_low]

                # Reset flags (regs 15, 16, 17)
                self.state.memory[15] = 0
                self.state.memory[16] = 0
                self.state.memory[17] = 0

                if d == e:
                    self.state.memory[15] = 1 # Equal Flag (ZF)
                elif d > e:
                    self.state.memory[16] = 1 # Greater Flag (CF)
                elif d < e:
                    self.state.memory[17] = 1 # Less Flag (SF)

            elif a == 22:
                # Return
                return self.state.memory[b]

            # Increment Program Counter
            self.state.pos += 2

        return -1

# --- Usage Example ---
if __name__ == "__main__":
    vm = VM()
    
    # The bytecode from BCeption_solution.md
    opcodeshs = '1401010F04150F0E531401140214031404010813010937010A01010BF0010C0F010D900107AD15270E2C03EA07190107E915170E3703EA074807490107CB15470E4403EA073D073C073901071615370E5303EA160E'
    bytecode = list(bytearray.fromhex(opcodeshs))

    print("--- VM State Dump (Memory & PC) ---")
    
    # The solved password is 3735928559 (0xDEADBEEF)
    correct_input = 3735928559
        
    vm.load_input(correct_input)

    # Initial memory state for the input check area
    print(f"Loaded input 0x{correct_input:X} -> MEM[1:5]: {vm.state.memory[1:5]}")
    
    # Initialize R8 for stack operations as suggested by solution
    vm.state.memory[8] = 0x13 
    
    print(f"Running VM with correct input: {correct_input}")
    result = vm.check(bytecode)
    
    print("\n--- Execution Result ---")
    print(f"Final Return Value (MEM[0xE]): {result}")
    
    # Expected result is 4 for "Well Done"
    if result == 4:
        print("PASS: VM returned 4 (SUCCESS)")
    else:
        print("FAIL: VM did not return 4. Returned value was: {result}")
