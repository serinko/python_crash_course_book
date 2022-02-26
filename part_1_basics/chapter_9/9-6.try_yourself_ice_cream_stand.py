class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributtes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Displays information about the restaurant cuisine"""
        print(f"{self.name.title()}, world number one in {self.cuisine}.")

    def open_restaurant(self):
        """Dislays that the restaurant is open"""
        print(f"{self.name.title()} is now open!")


class IceCreamStand(Restaurant):
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


panda_ice = IceCreamStand('panda ice', 'ice cream')
panda_ice_flavors = ['strawberry', 'pineapple', 'coconut', 'lemon', 'almond']
panda_ice.describe_restaurant()
panda_ice.open_restaurant()
panda_ice.display_favors(panda_ice_flavors)
