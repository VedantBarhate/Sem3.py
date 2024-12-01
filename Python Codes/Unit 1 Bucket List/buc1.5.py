# Define a base class Animal with an attribute name and a method make_sound(). Create a derived class Dog that inherits from Animal and overrides the make_sound() method to print ""Woof"". Instantiate a Dog object and demonstrate calling the overridden method.
# Concepts Covered: Inheritance, Method Overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

my_dog = Dog("Buddy")
my_dog.make_sound()
