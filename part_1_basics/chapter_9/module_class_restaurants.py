"""A module containing simple class Restaurant and Icecream stand"""


class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributtes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restauant(self):
        """Displays information about the restaurant cuisine"""
        print(f"{self.name.title()}, world number one in {self.cuisine}.")

    def open_restaurant(self):
        """Dislays that the restaurant is open"""
        print(f"{self.name.title()} is now open!")


class IceCreamStand(Restaurant):
    """A simple attempt to model an icecream stand"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes of the sub class"""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_favors(self, flavors):
        self.flavors = flavors

        print(
            f"\nThese are the flavors we have today:"
        )
        for flavor in self.flavors:
            print(f"\t - {flavor.title()}")
