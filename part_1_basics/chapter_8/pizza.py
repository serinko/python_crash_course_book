def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'cheese', 'tuna')

# The * sign makes an empty tupple as a para,eter
# Therefore as such is printed, whether it has one argument or several
