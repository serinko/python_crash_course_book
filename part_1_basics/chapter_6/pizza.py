# Store information about each pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', ],
}
# second value in the dictionary is a list

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      f"with the fillowing toppings:")

# for loop the items
# point to the list as to any value of a dictionary
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")
