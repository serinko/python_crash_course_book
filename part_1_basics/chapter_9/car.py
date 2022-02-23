# WORKING WITH CLASS INSTANCES

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

print("\n\n")


#
#
# SETTING A DEFAULT VALUE FOR AN ATTRIBUTE
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # We added a default odometer value method

    #
    # 2) To be able to update a value of attribute through a method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# MODIFYING ATTRIBUTE VALUES:
# Can be done in three ways:
# 1) Directly through an instance
# 2) Set the value through a method
# 3) Increment the value (add a certain amount to it) through a method

# 1) Directly:
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# We use .notation to access the attribute and directly set a new value to it
# Sometimes this fits, other times a method can update the value
print("\n")

# 2) Modifying an attributtes vale through a method
my_new_car.update_odometer(23)
my_new_car.read_odometer()
