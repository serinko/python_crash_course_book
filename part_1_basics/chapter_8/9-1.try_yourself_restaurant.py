class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributtes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restauant(self):
        """Displays information about the restaurant cuisine"""
        print(f"{self.name.title()} offers a good services.")

    def open_restaurant(self):
        """Dislays that the restaurant is open"""
        print(f"{self.name.title()} is now open!")


restaurant = Restaurant('nagano', 'sushi')
print(f"{restaurant.name.title()} is a new restaurant.")
print(f"{restaurant.name.title()} is specialized in {restaurant.cuisine}.")
restaurant.describe_restauant()
restaurant.open_restaurant()
