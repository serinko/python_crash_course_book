prompt = "\nWelcome to our pizza. Choose the size of your pizza? "
prompt += "\nType '1' for small, '2' for medium and '3' for XL size: "
size = input(prompt)
size = int(size)

if size == 1:
    active = True
    price = 8
    size = 'small'
elif size == 2:
    active = True
    price = 10
    size = 'medium'
elif size == 3:
    active = True
    price = 12
    size = 'XL'
else:
    print("We are sorry, this was not a correct choice, try again")
    active = False

topping = ""

while active:
    message = f"\nYour pizza size is: {size}."
    message += "\nPlease choose a topping from our menu. "
    message += "\nEach topping costs $1. "
    message += f"\n(when you finished, type 'done', please.) "
    topping = input(message)
    price += 1
    if topping.lower() == 'done':
        price -= 1
        print(f"Your pizza is almost finished. Price is ${str(price)}.")
        active = False
    else:
        print(f"We will add {topping} to your pizza.")
