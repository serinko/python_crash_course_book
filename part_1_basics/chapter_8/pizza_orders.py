def welcoming_message():
    """Welcoming user in the cli pizza order"""
    message = "Hello, welcome to Pizza Locco, please enter your order"
    print(message)


def choose_pizza_size(size):
    """Prompt user to choose the size of a pizza"""
    active = True
    while active:
        prompt_size = "Please choose if you want a size of 33 or 44cm pizza: "
        prompt_size += "Enter 'q' to quickly finish your order"
        size_user = input(prompt_size)
        if size_user.lower() == 'q':
            print("Good bye")
            quit()

        else:
            size_user = int(size_user)
            print(f"You have chosen pizza size {str(size_user)}.")
            size_user = size
            active = False
            return size_user


def choose_pizza_toppings():
    """Prompt user to add toppings, append them to a list"""
    prompt_toppings = "Please choose your toppings."
    prompt_toppings += "Press enter after ach topping."
    prompt_toppings += "Enter 'done' when finished."
    active = True

    while active:
        topping = input(prompt_toppings)
        tpgs = []
        tpgs.append(topping)

        if tpgs:
            print(f"\nWe added {topping} on your pizza.")
            prompt = "For another topping press enter, " \
                     "or press 'q' to finish your order."
            more = input(prompt)
            if more.lower() == 'q':
                active = False

        else:
            print("You have chosen a pizza without any topping")
            active = False

    return tpgs


def make_pizza(size, toppings=None):
    """Summarize the pizza we are about to make."""
    size_user = size
    tpgs = toppings
    print(f"\nThank you for your order."
          f"We are preparing you pizza size {size} "
          f"with the following toppings:")
    if toppings:
        for t in toppings:
            print(f" - {t}")
    else:
        print(" - no toppings")
