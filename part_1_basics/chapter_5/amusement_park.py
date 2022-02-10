# an amusement park charges different rates for different age groups
# anyone under 4 is free
# anyone between 4 and 18 is $5
# anyone older 18 is $10
# Use if statement to determine the rate

age = 55
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# if-elif_else: chain, in practice:
# if: True, code gets executed and Python skips the rest
# if: False, code reads elif
# elif: True, code gets executed and skips else
# elif: False, code reads down to else and executes whats under else:
