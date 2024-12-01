# Define a class Person with a class variable population_count. Implement an __init__ method to initialize a person’s name. Add a class method increment_population to increase population_count whenever a new person is created. Demonstrate the usage of the class method by creating multiple instances of Person.
# Concepts Covered: Class Method, Class Variables

class Person:
    population_count = 0

    def __init__(self, name):
        self.name = name
        Person.increment_population()

    @classmethod
    def increment_population(cls):
        cls.population_count += 1


print("Population Count:", Person.population_count)
person1 = Person("Vedant")
print("Population Count:", Person.population_count)
person2 = Person("Vibhor")
print("Population Count:", Person.population_count)