# multiple conditions
# in case there is more then one, more if tatements needs to be checked

requested_toppings = ['mushrooms', 'onions', 'pineapple', 'pepperoni']

if 'mushrooms' in requested_toppings:
    print("Add mushrooms.")

if 'onions' in requested_toppings:
    print("Add onions.")

if 'pineapple' in requested_toppings:
    print("Add pineapple.")

if 'pepperoni' in requested_toppings:
    print("Add pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Add extra cheese.")
# endless if statements can be added and as list gets modified, message changes
# They get evaluated regardless of the previous if result
print("\nFinished your pizza.")

print("\n")

# More efficient way would be the for loop:
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished your pizza.")

print("\n")

# Pepperoni ran out:
for requested_topping in requested_toppings:
    if requested_topping == "pepperoni":
        print("We are sorry but we are out of pepperoni.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished your pizza.")

print("\n")

# Making a check if the list is empty
requested_toppings = []  # empty list

if requested_toppings:  # checks if list == True/False
    # if True:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")

    print("\nFinished your pizza.")
# if list is False (empty):
else:
    print("Are you sure you want a plain pizza?")
# Prints message to make sure

print("\n")

# using multiple lists
available_topings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_topings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we dont have " + requested_topping + ".")

print("\nFinished your pizza.")

print("\n")
