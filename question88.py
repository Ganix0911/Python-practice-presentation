## Constructor: Define a class Car with a constructor that sets make, model, and year. Create an instance and display its details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car('Toyota', 'Corolla', 2019)
print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")