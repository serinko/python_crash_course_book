def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nWe are preparing you pizza size {size} "
          f"with the following toppings:")
    if toppings:
        for topping in toppings:
            print(f" - {topping}")
    else:
        print(" - no toppings")
