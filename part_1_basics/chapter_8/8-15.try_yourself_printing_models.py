# Using the import module + as, seems the most general standard.

import printing_functions as pf

# Importing module printing functions
# using alias pm
# The module has two functions which I will use both

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Lists I will work with

pf.print_models(unprinted_designs, completed_models)
# Calling a function, using the two lists as arguments

pf.show_completed_models(completed_models)
# Calling the function to show the new list in a nice
#
