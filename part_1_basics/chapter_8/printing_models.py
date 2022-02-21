# # This is a way with a while loop, without any def function
# # Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # simulateprinting each design, until none are left.
# # Move each design to complete_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
#
# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# USING FUNCTIONS
# We make two functions to allow flexibility
# Following the same code structure as above
# Storing that in functions
def print_models(unprinted_designs, completed_models):
    """
    Simulare printing each design , until none are left.
    Move each design to complete_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# Creating lists which have identical names with the parameter
# This is how organized is the body of the program
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Using these lists as arguments when calling the function
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Such program is easier to read and better organized
# we can always recycle it with more models
# those can be add to the list by users
# Every function should have one specific job
# It is more benefitial than pushing it all into one function

# PREVENTING FUNCTION FROM MODIFYING THE LIST
# When calling the function, we use a copy [:] of the list
# Original then stays intact.

print_models(unprinted_designs[:], completed_models)
# This will use a ful slice (copy) and keep the original
