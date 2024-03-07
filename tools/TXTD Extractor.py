# extractor.py
import struct

def extract(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(4)
        if header != b'TXTD':
            print("Invalid file format")
            return
        
        num_strings = struct.unpack('<I', file.read(4))[0]  # Reading the number of strings correctly
        
        addresses = [struct.unpack('<I', file.read(4))[0] for _ in range(num_strings)]  # Reading addresses
        
        strings = []
        for address in addresses:
            file.seek(address)
            string_bytes = bytearray()
            while (byte := file.read(1)) != b'\x00':
                string_bytes += byte
            try:
                string = string_bytes.decode('shift_jis')
            except UnicodeDecodeError:
                string = string_bytes.decode('ascii', errors='ignore')
            strings.append(string)
        
        with open(file_path + ".txt", 'w', encoding='utf-8') as output_file:
            for idx, string in enumerate(strings):
                output_file.write("{:02}:{}".format(idx, string.replace('\n', '\\n')))
                output_file.write("\n\n")  # Add extra newline between entries

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python extractor.py <file>")
    else:
        extract(sys.argv[1])
