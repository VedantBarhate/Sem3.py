# Create a class Calculator with two instance variables a and b. Implement instance methods to perform addition and subtraction. Add a static method to multiply two numbers without using the instance variables. Create an object of Calculator and demonstrate the usage of instance and static methods.
# Concepts Covered: Instance Methods, Static Methods

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    @staticmethod
    def multiply(x, y):
        return x * y


cal = Calculator(17, 8)

print("Addition:", cal.add())
print("Subtraction:", cal.sub())

print("Multiplication:", Calculator.multiply(3, 4))