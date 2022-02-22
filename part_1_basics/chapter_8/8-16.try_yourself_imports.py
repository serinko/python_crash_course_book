# Importing pizza order frunctions

import pizza_orders as pz

pz.welcoming_message()

size = pz.choose_pizza_size()
# Defines size to be used later as an arument

toppings = pz.choose_pizza_toppings()
# Defines toppings to be used later as an arument

pz.make_pizza(size, toppings)
