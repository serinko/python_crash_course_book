# MODULE
# Contains functions to make a program for a pizza order


def welcoming_message():
    """Displays welcoming message in Pizza Loco order client"""
    message = "\n\n\n\n              P I Z Z A     L O C C O               " \
              "\n   ============================================= \n\n" \
              "Hello, welcome to Pizza Locco, " \
              "let's start with the order..."
    print(message)


def choose_pizza_size():
    """Returns size of users chosen pizza"""
    active = True
    while active:
        prompt_size = \
            "\nPlease choose the size of your pizza. 33 or 44. "
        prompt_size += \
            "\n(to enter finish your order, enter  'q') \n\n" \
            "SIZE: \t"
        size_user = input(prompt_size)
        if size_user.lower() == 'q':
            print("No size, no pizza!!"
                  "\nGood bye")
            quit()

        else:
            size_user = int(size_user)
            print(f"\nYou have chosen pizza size {str(size_user)}.")
            active = False

    return size_user


def choose_pizza_toppings():
    """Returns a list of users chosen toppings"""
    prompt_toppings = "\nPlease choose your toppings."
    prompt_toppings += "\n(Press enter after ach topping."
    prompt_toppings += "\nEnter 'q' when finished)\n"
    prompt_toppings += "\nTOPPING: "
    active = True
    tpgs = []
    while active:
        topping = input(prompt_toppings)

        if topping == 'q':
            print("You have chosen a pizza without any topping")
            active = False
        else:
            tpgs.append(topping)

        if tpgs:
            while active:
                print(f"\nWe added {tpgs[-1]} on your pizza.")
                prompt_more = "Enter another topping, " \
                              "or press 'q' to finish your order.\n" \
                              "\nTOPPING: "
                more = input(prompt_more)

                if more.lower() == 'q':
                    active = False
                else:
                    tpgs.append(more)

        else:
            active = False

    return tpgs


def make_pizza(size, toppings=None):
    """Displays a summary of clients pizza, size and toppings"""
    message = "\n\n\n   ========== ORDER FINISHED ========== "
    print(message)
    print(f"\n\nThank you for your order. "
          f"We are preparing you pizza size {size} "
          f"with the following toppings:")
    if toppings:
        for t in toppings:
            print(f" - {t}")
    else:
        print(" - no toppings chosen")

    print("\n\nEnjoy your pizza and see you soon!!!")
