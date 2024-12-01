# bucket list Q2

# Create a class Logger with a method log that prints a message before and after the execution of a function. 
# Use an instance of Logger as a decorator for a method compute in a class MathOperations. 
# Demonstrate by calling the decorated method.
# Concepts Covered: Class-based Decorators

class Logger:
    def log(self, func):
        def inner(*args, **kwargs):
            print(f"Logging before executing {func.__name__}...")
            result = func(*args, **kwargs)
            print(f"Logging after executing {func.__name__}...")
            return result
        return inner

class MathOperations:

    @Logger().log
    def add(self, x, y):
        print(f"adding {x} and {y}...")
        return x + y
    
    @Logger().log
    def sub(self, x, y):
        print(f"subtracting {x} and {y}...")
        return x - y

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    math_ops = MathOperations()

    r1 = math_ops.add(15, 20)
    print(f"Result: {r1}")
    r2 = math_ops.sub(30,12)
    print(f"Result: {r2}")
