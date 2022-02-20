def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')

# Function can be called multiple times
# Using new arguments for the same parameters:
describe_pet('dog', 'psouk')
# ORDER IS IMPORTANT!

# keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
# If we define the keywords
# to which parameter, given argumet is asigned, order can be changed
# Python prioritize the keyword defintion in this case
describe_pet(pet_name='harry', animal_type='hamster')
