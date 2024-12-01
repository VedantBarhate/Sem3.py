# Create an abstract base class Shape with an abstract method area(). Define two derived classes, Circle and Rectangle, that implement the area() method. Instantiate both classes and print their areas. Use the abc module for abstract base class implementation.
# Concepts Covered: Abstraction, Abstract Base Class

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

my_circle = Circle(5)
my_rectangle = Rectangle(4, 3)

print(my_circle.area())
print(my_rectangle.area())