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


restaurant_0 = Restaurant('nagano', 'sushi')
print(f"{restaurant_0.name.title()} is a new restaurant.")
print(f"{restaurant_0.name.title()} is specialized in {restaurant_0.cuisine}.")
restaurant_0.describe_restauant()
restaurant_0.open_restaurant()

restaurant_1 = Restaurant('palermo', 'pizza')
print(f"\n{restaurant_1.name.title()} is a new restaurant.")
print(f"{restaurant_1.name.title()} is specialized in {restaurant_1.cuisine}.")
restaurant_1.describe_restauant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('ranger', 'burger')
print(f"\n{restaurant_2.name.title()} is a new restaurant.")
print(f"{restaurant_2.name.title()} is specialized in {restaurant_2.cuisine}.")
restaurant_2.describe_restauant()
restaurant_2.open_restaurant()
