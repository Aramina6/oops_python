# Define the first base class
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start_engine(self):
        return "Engine started with horsepower: {}".format(self.horsepower)

# Define the second base class
class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def number_of_wheels(self):
        return "This vehicle has {} wheels.".format(self.wheel_count)

# Define the derived class that inherits from both Engine and Wheels
class Car(Engine, Wheels):
    def __init__(self, horsepower, wheel_count, make):
        # Initialize the base classes
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, wheel_count)
        # Additional attributes specific to Car
        self.make = make

    def car_details(self):
        return "Car make: {}, Horsepower: {}, Wheels: {}".format(
            self.make, self.horsepower, self.wheel_count
        )

# Create an instance of the Car class
my_car = Car(horsepower=300, wheel_count=4, make="Toyota")

# Call methods from the Engine base class
print(my_car.start_engine())  # Output: Engine started with horsepower: 300

# Call methods from the Wheels base class
print(my_car.number_of_wheels())  # Output: This vehicle has 4 wheels.

# Call method from the derived Car class
print(my_car.car_details())  # Output: Car make: Toyota, Horsepower: 300, Wheels: 4
