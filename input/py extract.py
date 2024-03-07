def extract_file(input_file, output_file, start_offset, end_offset):
    try:
        with open(input_file, 'rb') as f:
            f.seek(start_offset)
            data = f.read(end_offset - start_offset)
            with open(output_file, 'wb') as out:
                out.write(data)
            print(f"File extracted successfully from offset {hex(start_offset)} to {hex(end_offset)}")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
input_file = 'Shin Seiki GPX Cyber Formula [J] [PS2].iso'
output_file = 'extracted_file.bin'
start_offset = 0x18591800
end_offset = 0x18591FFE

extract_file(input_file, output_file, start_offset, end_offset)
