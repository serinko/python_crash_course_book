sandwich_orders = [
    'pastrami',
    'cheese and ham',
    'tuna',
    'pastrami',
    'pastrami',
    'vegan',
    'egg and onion',
    'salami',
]

finished_sandwiches = []

out_of = 'pastrami'

while sandwich_orders:
    while out_of in sandwich_orders:
        sandwich_orders.remove(out_of)
        message = (f"\nWe are sorry but we are out of "
                   f"{out_of.title()} sandwich at the moment.")

        print(message)

    current_sandwich = sandwich_orders.pop()
    print(f"\nWe are preparing the {current_sandwich.title()} "
          "sandwich at the moment.")
    finished_sandwiches.append(current_sandwich)

print("\nHere is the list of finished orders:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} sandwich is ready.")
