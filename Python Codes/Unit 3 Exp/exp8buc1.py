# Create a program that reads a text file and prints its contents to the console,
# demonstrating the use of read(), readline(), and readlines() methods.

def read_file_demo(file_path):
    print("Using read():")
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

    print("\nUsing readline():")
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end='')

    print("\n\nUsing readlines():")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')


if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    file_path = 'exp8_input.txt'
    read_file_demo(file_path)
