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
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll the odometer back!")
        # Extended the method/function by this if statement

    # 3) Increment attributes value
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


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

# 2) Modifying an attribute's vale through a method
# Created a new function update_odometer
my_new_car.update_odometer(23)
my_new_car.read_odometer()
# The new method (function) takes in the variable mileage sat as a default
# in the method read_odometer
# Sets a new value to that variable and returns the method back
#
# We can also extend it by if statement..
print("\n")

#
# 3) Incerementing an attribute's value through a method
# Value can be incremented by a certain ammount.
# We can set a method to increment the value
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# The new method takes the value form reading odometer
# add an increment defined as a method argument
# The same if method could be applied to this function.

# EFFECTIVE SECURITY
# The if statement can be seen as a concept, in a flexible way
# Addictional security to make sure a program takes account
# of all possible attempts of missuse.
