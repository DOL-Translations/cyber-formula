import sys

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        entries = content.split('\n\n')  # Assuming double newlines separate entries
        return [entry.strip() for entry in entries if entry.strip()]

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

def update_file(file_a_path, file_b_path):
    file_a_strings = read_file(file_a_path)
    file_b_strings = read_file(file_b_path)
    mapped_list = get_mapped_list()
    
    # Adjust for skipped mappings
    mapped_list = [x if isinstance(x, int) else None for x in mapped_list]

    # Update the strings in file A with corresponding strings from file B
    ignore_indices = {15, 16, 19, 24, 25, 28, 29, 38, 39, 82, 95, 116, 123, 128, 133, 141, 147}
    for i, map_index in enumerate(mapped_list):
        if map_index is not None and i < len(file_a_strings) and map_index < len(file_b_strings) and i not in ignore_indices:
            _, new_string = file_b_strings[map_index].split(':', 1)  # Omit the index number
            file_a_strings[i] = f"{file_a_strings[i].split(':', 1)[0]}:{new_string}"

    # Write the updated content back to file A
    with open(file_a_path, 'w', encoding='utf-8') as file_a:
        for entry in file_a_strings:
            file_a.write(entry + "\n\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python update_file.py <file_a_path> <file_b_path>")
        sys.exit(1)

    update_file(sys.argv[1], sys.argv[2])
