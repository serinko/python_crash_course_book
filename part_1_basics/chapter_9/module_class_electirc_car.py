""" A set of classes to be used to represent electreic car.
"""

# THIS IS  A MODULE, WHICH IS INHERITTED FROM AND IMPORTED MODULE
# BOTH NEED TO BE IMPORTED IN CASE OF FURTHER CALLS

from module_class_car import Car


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing batery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this batter provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrades electric car battery to 100-kWh"""
        if self.battery_size < 100:
            self.battery_size = 100
        print(
            "The battery size got upgraded."
        )


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric car does not have a gas tank."""
        print(f"Ths car does not have a gas tank.")
    # A mistake in the book, no fill the gas tank function in class Car()
