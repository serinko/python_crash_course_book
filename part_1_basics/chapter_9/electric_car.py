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


# Defining new class, which does not inherit from any other class
class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing batery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # Adding a new method to the Class
    def get_range(self):
        """Print a statement about the range this batter provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # adding a new attribute with a default value
        # self.battery_size = 75
        # Commenting on it as I made a new class for battery

        # adding the same attribute, defined as a class above
        self.battery = Battery()

    # # And adding a new method, working with the new attribute
    # def describe_battery(self):
    #     """Print a statement describing batery size"""
    #     print(f"This car haze a {self.battery_size}-kWh battery.")
    # Commented it all as I made a new entire class battery

    # Overriding a method from the parent class:
    def fill_gas_tank(self):
        """Electric car does not have a gas tank."""
        print(f"Ths car does not have a gas tank.")
    # A mistake in the book, no fill the gas tank function in class Car()


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

# ~ my_tesla.describe_battery()
# This description shows that it is clearly an electric car.
# There is no limit in the definition of the sub class
# Attributes fitting the super class can be added there
# Later usage of the superclass method will contain them

# OVERRIDING METHODS FROM THE PARENT CLASS
# Any method can be overridden.
# Define the method with the same name in the child class
# Python will disregard the parent class and use the new, same name method

# INSTANCES AS ATTRIBUTES
# Sometimes too many attributes in one class create lenghty code
# We may create more classes instead
# Those can be used in another programs then.
# here it can be for example the battery.
# Important is that the class which we reffer to later must come above!
# any electric_car instance will have a Battery instance created automatically

# When we want to descibe the battery, we need to work through
# the battery attribute.
my_tesla.battery.describe_battery()
# Python looks at the instance my_tesla
# find its battery attribute and call the method describe_batter()
# that's associated with the Battery instance stored in the attribute

# This loks like a lot of work, but as usually, having indenpendendt code
# means we can modify it separatelly
# adding another method get_range
my_tesla.battery.get_range()
# method get_range() performs a simple analyses.
# Then reports the value 