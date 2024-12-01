import threading

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Reading from {file_name}:")
            print(file.read())
            print("-" * 50)
    except FileNotFoundError:
        print(f"Error: {file_name} not found!")

def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    threads = []
    for file_name in files:
        thread = threading.Thread(target=read_file, args=(file_name,))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("All files read successfully!")

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    main()