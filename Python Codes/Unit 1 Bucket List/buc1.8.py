# Create a base class Shape with a method draw(). Define two derived classes, Circle and Square, each implementing the draw() method in their own way. Create a list of Shape objects and call the draw() method on each object to demonstrate polymorphism.
# Concepts Covered: Polymorphism, Method Overriding

class Shape:
    def draw(self):
        print("Drawing a generic shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()