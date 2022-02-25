# Import multiple functions from a module:
from module_class_car import Car, ElectricCar

my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.read_descriptive_name()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n")

my_new_car = Car('audi', 'a4', 1986)
my_new_car.read_descriptive_name()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\n")

# Import entire module:
import module_class_car as mcc

my_tesla = mcc.ElectricCar('tesla', 'roadster', 2019)
my_tesla.read_descriptive_name()

print("\n")

my_new_car = mcc.Car('audi', 'a4', 1986)
my_new_car.read_descriptive_name()

print("\n")

# IMPORT MODULE FROM MODULE
# MODULE_CLASS_ELECTRIC_CAR HAS THE AN IMPORTED PARENT CLASS CAR
# THEREFORE WE NEED TO IMPORT BOTH OF THE CLASSES FROM THEIR ORIGINAL MODULES
# FOR THIS PROGRAM TO WORK

from module_class_car import Car
from module_class_electirc_car import Battery, ElectricCar

my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.read_descriptive_name()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n")

my_new_car = Car('audi', 'a4', 1986)
my_new_car.read_descriptive_name()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
