# Store information about each pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', ],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      f"with the fillowing toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping.title()}")
