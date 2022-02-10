# an amusement park charges different rates for different age groups
# anyone under 4 is free
# anyone between 4 and 18 is $5
# anyone older 18 is $10
# Use if statement to determine the rate

age = 70
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# if-elif_else: block, in practice:
# if: True, code gets executed and Python skips the rest
# if: False, code reads elif
# elif: True, code gets executed and skips else
# elif: False, code reads down to else and executes whats under else:

print("\n")

# For concice if-elif-else chain (not block) we define price
# and only one statement, which prints after the chain has been evaluated
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
# in this way th code is easier to modify.
print("Your admission cost is $" + str(price) + ".")
# takes value stored in price with str() function

print("\n")

# We can also use multiple elif blocks
# for example if we want to add a cheap admission for retired visitors
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 3
# in this way the code is easier to modify.
print("Your admission cost is $" + str(price) + ".")
