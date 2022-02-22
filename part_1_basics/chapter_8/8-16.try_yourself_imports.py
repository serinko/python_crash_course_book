# Importing pizza order frunctions
# Excercise is to use all different import approaches:

import pizza_orders as pz

pz.welcoming_message()

from pizza_orders import choose_pizza_size

size = choose_pizza_size()
# Defines size to be used later as an argument


from pizza_orders import choose_pizza_toppings as tpg

toppings = tpg()
# Defines toppings to be used later as an argument

import pizza_orders as pz

pz.make_pizza(size, toppings)
# My most favorite - easiest to read way of importing
