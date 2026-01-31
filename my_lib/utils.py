def parse_local_str(vals):
    b = b"".join(v.to_bytes(8, "little") for v in vals)
    return b.rstrip(b"\x00").decode("ascii")

def extract_bytes(input_file, output_file, offset, length):
    try:
        with open(input_file, 'rb') as f:
            # Move the file pointer to the start of goodBoy
            f.seek(offset)
            
            # Read 271 bytes
            data = f.read(length)
            
            # Save the extracted bytes to a new file
            with open(output_file, 'wb') as out:
                out.write(data)
                
        print(f"Successfully extracted {len(data)} bytes from offset {hex(offset)}.")
        print(f"Saved to: {output_file}")
        
    except FileNotFoundError:
        print("Error: The file 'sh4ll9.bin' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
