# repacker.py
import sys
import struct

def reverse_address_for_writing(address):
    # Reverse the address bytes and pad with two zeroes
    reversed_address = address.to_bytes(4, 'little')
    return reversed_address

def reverse_num_strings_for_writing(num):
    return num.to_bytes(4, 'little')

def encode_string(string):
    try:
        return string.encode('ascii') + b'\x00'
    except UnicodeError:
        return string.encode('shift_jis') + b'\x00'

def repack(input_txt_path, output_bin_path):
    with open(input_txt_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    strings = []
    for line in lines:
        line = line.strip()
        if line and ':' in line:
            idx, string = line.split(':', 1)
            strings.append(string.strip().replace('\\n', '\n'))
        elif line:
            print(f"Ignoring malformed line: {line}")

    num_strings = len(strings)
    
    with open(output_bin_path, 'wb') as file:
        file.write(b'TXTD')
        file.write(reverse_num_strings_for_writing(num_strings))
        
        current_address = 4 + 4 + num_strings * 4  # Header size + num_strings size + address blocks size
        
        for string in strings:
            address_to_write = reverse_address_for_writing(current_address)
            file.write(address_to_write)
            current_address += len(string.encode('shift_jis')) + 1
        
        for string in strings:
            file.write(encode_string(string))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python repacker.py <input_file.txt> <output_file.bin>")
    else:
        repack(sys.argv[1], sys.argv[2])
