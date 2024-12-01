# file handling

def task(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()
        num_lines = len(lines)
        print(f"Number of lines: {num_lines}")
        extracted_lines = lines[:2]

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(extracted_lines)

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    input_file = 'exp8_input.txt'
    output_file = 'exp8_output.txt'
    task(input_file, output_file)
