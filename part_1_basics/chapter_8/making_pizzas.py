import pizza_module

# importing module from the same folder

pizza_module.make_pizza(33, 'ham', 'pineapple', 'cheese')
pizza_module.make_pizza(46)

# call the module.function(arguments)

# or a specific one with the call:
# from module_name import function_name

from pizza_module import make_pizza

make_pizza(33, 'tuna', 'bacon', 'mozzarella')
# Then we call the function using only the function name

# MULTIPLE FUNCTIONS:
# If the module had multiple functions, we can import specific ones like this
# from pizza_module import make_pizza_0, make_pizza_1, make_pizza_2

# USINNG "as" TO GIVE A FUNCTION AN ALIAS
#
from pizza_module import make_pizza as mp

# from module_name import function_name as fn
mp(46, 'anchovy', 'ham', 'cream')

