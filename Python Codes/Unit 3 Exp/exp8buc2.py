# Implement a program that allows users to append additional data
# to an existing text file, preserving the original content.

def append_to_file(file_path, data_to_append):
    with open(file_path, 'a') as file:
        file.write(data_to_append + '\n')
    print("Data has been appended to the file.")

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    file_path = 'buc2_input.txt'
    data_to_append = "this is new data"
    append_to_file(file_path, data_to_append)

