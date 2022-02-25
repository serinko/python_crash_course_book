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
