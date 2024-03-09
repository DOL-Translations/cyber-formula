import sys

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Split the content by empty lines to handle extra newlines between entries
        content = file.read().strip()
        entries = content.split('\n\n')  # Assuming double newlines separate entries
        # Remove the initial '##:' from each entry
        cleaned_entries = [entry[entry.find(':')+1:].strip() for entry in entries if entry.find(':') != -1]
        return cleaned_entries

def get_mapped_list():
    # Include your complete mapping here. The '-' represents skipped values.
    return [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
        21, 22, 23, 24, '-', 28, 29, 30, 31, 40, 41, 42, 50, 51, 52, 53, 54, 55, 56, 
        57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 74, 80, 81, 87, 
        88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 
        106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 
        121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 
        136, 137, 138, 139, 140, 141, 142, 148, 156, 150, 151, 152, 153, 154, 155, 
        156, 157, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 
        174, 175, 176, 177, 178, 179, 166, 182, 183, 184, 185
    ]

def compare_files(file_a_path, file_b_path):
    file_a_strings = read_file(file_a_path)
    file_b_strings = read_file(file_b_path)
    mapped_list = get_mapped_list()
    
    # Adjust for skipped mappings
    mapped_list = [x if isinstance(x, int) else None for x in mapped_list]

    for i, map_index in enumerate(mapped_list):
        if map_index is None or map_index >= len(file_b_strings):
            continue  # Skip if mapping is not valid or out of bounds
        
        if i < len(file_a_strings) and file_a_strings[i] != file_b_strings[map_index]:
            print(f"Difference at A[{i}] -> B[{map_index}]:")
            print(f"    A: {file_a_strings[i]}")
            print(f"    B: {file_b_strings[map_index]}")
            print()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python compare_mapped_strings.py <file_a_path> <file_b_path>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
