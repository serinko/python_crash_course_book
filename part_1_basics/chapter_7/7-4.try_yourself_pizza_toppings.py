prompt = "\nYour order is alomst finished, would you like any extra toppings? "
prompt += "\n(Please enter 'done' to confirm.) "
active = True
# message = ""

while active:
    topping = input(prompt)

    if topping.lower() == 'done':
        active = False
    else:
        print(f"We will add {topping} to your pizza.")
