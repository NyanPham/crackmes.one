import struct

def get_crc32_input_string(target_hex_str):
    """
    Reverses a standard CRC-32 loop to find the 4-byte input string
    that generates the given target checksum.
    """
    # 1. Parse the target checksum
    # Note: 0x0A50FAC56 fits in 32 bits because the leading hex digit is 0.
    target_chksum = int(target_hex_str, 16)
    
    # Standard CRC-32 Polynomial (reversed representation)
    POLY = 0xEDB88320
    
    # 2. Unwind the CRC-32 loop
    # We reverse the operations for 32 bits (4 bytes * 8 bits).
    # Forward:  LSB check -> Shift Right -> XOR Poly
    # Backward: MSB check -> XOR Poly -> Shift Left
    
    state = target_chksum
    
    for _ in range(32):
        # Check if the MSB (Bit 31) is 1.
        # If it is, it means the polynomial was XORed in the forward step.
        if state & 0x80000000:
            state = (state ^ POLY)
            state = (state << 1) | 1 # Shift left and force LSB to 1
        else:
            state = (state << 1)     # Shift left, LSB is 0
        
        # Ensure we stay within 32-bit bounds
        state &= 0xFFFFFFFF

    # 3. Recover the input bytes
    # The 'state' is now the register value BEFORE the input was XORed.
    # Since the C code initializes chksum to 0xFFFFFFFF, we XOR that out.
    # Input = Unwound_State ^ Initial_Value
    result_int = state ^ 0xFFFFFFFF
    
    # 4. Convert the integer to 4 bytes (Little Endian)
    buf_bytes = struct.pack('<I', result_int)
    
    return buf_bytes

# ==========================================
# Main Execution
# ==========================================

target_str = "0x0A50FAC56"
print(f"Target Checksum: {target_str}\n")

try:
    # Calculate the bytes
    result_bytes = get_crc32_input_string(target_str)
    
    # 1. Print as Hex Array (C-Style)
    hex_array = ", ".join([f"0x{b:02X}" for b in result_bytes])
    print(f"C Array:       {{ {hex_array}, 0 }}")
    
    # 2. Print as Python Bytes
    print(f"Bytes Object:  {result_bytes}")
    
    # 3. Print as Real String (Chars)
    # We use 'latin-1' encoding because it maps bytes 0-255 1-to-1 with characters.
    # UTF-8 would fail on bytes like 0xBA or 0xFC.
    decoded_str = result_bytes.decode('latin-1')
    print(f"Real String:   {decoded_str}")

except Exception as e:
    print(f"An error occurred: {e}")
