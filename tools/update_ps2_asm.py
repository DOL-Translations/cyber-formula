import sys

def find_string_in_ps2_iso(ps2_iso_path, search_string, start_addr, end_addr):
    with open(ps2_iso_path, 'rb') as iso:
        iso.seek(start_addr)
        while iso.tell() <= end_addr:
            current_addr = iso.tell()
            line = iso.readline()  # Read chunks that likely contain the string
            if search_string.encode('ascii') in line:  # Assuming ASCII for simplicity; adjust for Shift_JIS if needed
                return current_addr + line.find(search_string.encode('ascii'))
            if not line:  # End of file
                break
    return None

def extract_string_from_iso(gcn_iso_path, addr):
    with open(gcn_iso_path, 'rb') as iso:
        iso.seek(addr)
        return iso.read().split(b'\x00', 1)[0].decode('ascii', errors='ignore')

def update_ps2_asm(gcn_iso_path, ps2_iso_path, gcn_asm_path, output_ps2_asm_path):
    last_found_addr_ps2 = 0x003CAA00 # Initialize with the starting address in PS2 ISO for the first search

    with open(gcn_asm_path, 'r', encoding='utf-8', errors='ignore') as gcn_asm, open(output_ps2_asm_path, 'w', encoding='utf-8') as output_ps2_asm:
        for line in gcn_asm:
            if line.startswith('//') or not line.strip():
                output_ps2_asm.write(line)  # Copy comments and empty lines as-is
                continue
            
            # Extract address and text from the line
            parts = line.split(',', 1)
            if len(parts) < 2:
                print(f"Skipping malformed line: {line.strip()}")
                continue  # Skip lines that don't have the correct format
            
            addr_hex = parts[0].strip().split('$')[-1]  # Extract hexadecimal address
            text = parts[1].strip()

            addr = int(addr_hex, 16)  # Convert hexadecimal address to integer
            string = extract_string_from_iso(gcn_iso_path, addr).replace('\n', '\x0A')  # Replace newline with 0x0A
            new_addr = find_string_in_ps2_iso(ps2_iso_path, string, last_found_addr_ps2, 0x003D2F59)

            if new_addr is not None:
                output_ps2_asm.write(f'Text(${new_addr:06X}, {text}')
                last_found_addr_ps2 = new_addr  # Update last found address for the next search
            else:
                output_ps2_asm.write(f'// {line.strip()} // Not found\n')


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python update_ps2_asm.py <gcn_iso_path> <ps2_iso_path> <gcn_asm_path> <ps2_asm_path>")
        sys.exit(1)

    update_ps2_asm(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
