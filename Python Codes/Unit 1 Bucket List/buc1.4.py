# Create a class Rectangle with attributes width and height. Implement the __init__ method to initialize these attributes. Override the __str__ and __repr__ methods to provide a string representation of the rectangle. Create an instance and print it to see the custom string representation.
# Concepts Covered: Magic Methods (__init__, __str__, __repr__)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

# Create an instance
my_rect = Rectangle(4, 3)
print(my_rect)
print(repr(my_rect))