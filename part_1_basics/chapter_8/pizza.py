def make_pizza_simple(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)


make_pizza_simple('pepperoni')
make_pizza_simple('mushrooms', 'cheese', 'tuna')


# The * sign makes an empty tupple as a para,eter
# Therefore as such is printed, whether it has one argument or several

# Replace the print with a loop to have a nicer order of the toppings
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'cheese', 'tuna')


# The outcome is not a tuple, but a nice structured summary

# MIXING POSITIONAL AND ARBITRARY ARGUMENTS
# Positional parameter must come first
# *arbitrary argument always last
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nWe are preparing you pizza size {size} "
          f"with the following toppings:")
    if toppings:
        for topping in toppings:
            print(f" - {topping}")
    else:
        print(" - no toppings")


make_pizza(33, 'pepperoni')
make_pizza(46, 'mushrooms', 'cheese', 'tuna')
make_pizza()
