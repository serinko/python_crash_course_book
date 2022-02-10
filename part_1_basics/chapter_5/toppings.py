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
