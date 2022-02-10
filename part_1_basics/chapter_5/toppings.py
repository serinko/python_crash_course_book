# multiple conditions
# in case there is more then one, more if tatements needs to be checked

requested_topping = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in requested_topping:
    print("Add mushrooms.")

if 'onions' in requested_topping:
    print("Add onions.")

if 'pineapple' in requested_topping:
    print("Add pineapple.")

if 'pepperoni' in requested_topping:
    print("Add pepperoni.")

if 'extra cheese' in requested_topping:
    print("Add extra cheese.")
# endless if statements can be added and as list gets modified, message changes
# They get evaluated regardless of the previous if result
print("\nFinished your pizza.")
