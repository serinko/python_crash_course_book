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

    def read_descriptive_name(self):
        """Displays the full descriptive name."""
        print(
            f"Car: {self.get_descriptive_name()}"
        )

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


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.read_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
