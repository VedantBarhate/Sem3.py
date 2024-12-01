import threading
import time

def count_numbers():
    for i in range(1, 6):
        print(f"Counting: {i}")
        time.sleep(1)
def calculate_square():
    for i in range(1, 6):
        print(f"Square of {i}: {i**2}")
        time.sleep(1)
def calculate_cube():
    for i in range(1, 6):
        print(f"Cube of {i}: {i**3}")
        time.sleep(1)

def main():
    thread1 = threading.Thread(target=count_numbers)
    thread2 = threading.Thread(target=calculate_square)
    thread3 = threading.Thread(target=calculate_cube)
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print("All tasks completed!")

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    main()