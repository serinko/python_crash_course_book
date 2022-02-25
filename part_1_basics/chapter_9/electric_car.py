# INHERITANCE
# Making a child class inheriting from an existing - parent class

# Original - parent class:

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

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # adding a new attribute with a default value
        self.battery_size = 75

    # And adding a new method, working with the new attribute
    def describe_battery(self):
        """Print a statementdescribing batery size"""
        print(f"This car haze a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# How it works:
# We start with the parent class Car
# Must appear above in the program than the inheriting child class
# Defining the child class, the name of the parent class
# must be included in the paranthesis
# The __init__() method takes takes info required to make a parent Class
# instance.
# super() function allows to call a method from the parent class.
# Tells Python to call the attributes from the parent / suprclass
# to use them in the child / subclass
# Instance ElectricCar given the atributtes calling for parent class and
# calling a method described in the parent class

# Once we have a child class, we can define new attributes and methods
# Those will differentiate from the parrent class

my_tesla.describe_battery()
