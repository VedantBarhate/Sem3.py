# Define a class named Car with attributes make, model, and year. Create a constructor to initialize these attributes. Create an instance of Car and display its attributes.
# Concepts Covered: Class, Object, Constructor, Instance Variables


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Camry", 2023)
print(my_car.make)
print(my_car.model)
print(my_car.year)
