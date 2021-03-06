class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Dog is a class
# Any instance (particular dog) can be used for this class
# Fuctions in a class are called methods
# __init()__ must have the underscores so Python recognizes it automatically
# self parameter Python reads as a refference to itself
# PAsses automatically
# There is two more parameters, name and age
# both with prefix self.
# any variable with prefix self is available to any method within the class
# The methods sit() and roll_over() don't do much now
# They can be extended with given instance later and describe more complex
# object or it's behaviour


# SETTING AN INSTANCE

my_dog = Dog('Willie', 6)
print(f"My dog's name is a {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# When setting the variable my_dog, Dog class is used with new arguments
# Python runs it through the __init()__ and creates an instance
# Representing this particular dog with the values provided
# Convention of capitalized Dog reffers to a class
# lower case my_dog to an instance
# To access attributes e use dot notation (my_dog.name)
# This syntax tells Python how to find attributes value
#
# CALLING A METHOD (function)
#
# my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
# Give the name of the instance and the method you want to call.
# When variables and methods described well,
# we can easily infer what the block of code is supposed to do.
#
print("\n")
#
# CREATING MULTIPLE INSTANCES
# As many instances can be created
your_dog = Dog('Lucy', 3)

print(f"My dog's name is a {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is a {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()
