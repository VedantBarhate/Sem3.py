# bucket list Q4

# Create a class Fibonacci that generates the Fibonacci sequence up to a specified number of elements.
# Implement the __iter__ and __next__ methods to make Fibonacci an iterator.
# Print the first 10 numbers in the Fibonacci sequence.
# Concepts Covered: Custom Iterable, Iterators

class Fibonacci:
    def __init__(self, num_ele):
        self.num_ele = num_ele
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.num_ele:
            raise StopIteration
        self.count += 1
        a = self.a
        self.a, self.b = self.b, self.a + self.b
        return a

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    fib = Fibonacci(6)
    for num in fib:
        print(num)