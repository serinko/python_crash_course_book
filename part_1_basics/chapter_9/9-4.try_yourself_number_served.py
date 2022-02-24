class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributtes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restauant(self):
        """Displays information about the restaurant cuisine"""
        print(f"{self.name.title()} offers quality services.")

    def read_description(self):
        """Displays more info to attract the guests"""
        print(
            f"{self.name.title()} is a new restaurant."
        )
        print(
            f"{self.name.title()} is specialized in "
            f"{self.cuisine}."
        )

    def open_restaurant(self):
        """Dislays that the restaurant is open"""
        print(f"{self.name.title()} is now open!")

    def set_number_served(self, guests):
        """Set the number of served guest to a given value"""
        self.number_served = guests

    def read_number_served(self):
        """Print a statement with the number of served guests."""
        print(
            f"Restaurant {self.name.title()} "
            f"was visited by {self.number_served} guests."
        )

    def increment_number_served(self, number):
        """Adds a given amount tho the total of guests"""
        if number > 0:
            self.number_served += number
        else:
            print("Increment must have positive value")


restaurant_0 = Restaurant('nagano', 'sushi')
restaurant_0.read_description()
restaurant_0.describe_restauant()
restaurant_0.open_restaurant()
restaurant_0.read_number_served()
restaurant_0.set_number_served(75)
restaurant_0.read_number_served()
restaurant_0.increment_number_served(0)
restaurant_0.read_number_served()
restaurant_0.increment_number_served(25)
restaurant_0.read_number_served()
