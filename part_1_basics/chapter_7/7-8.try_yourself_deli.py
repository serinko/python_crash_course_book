# EXCERCISE
# MAke a list called sandwich_orders and fill it with names of sandwiches
# Loop through the list of orders and print a message for each order
# such "I made your xxx sandwich".
# Each made sandwich move to the list of finished_sandwiches
# After it is all finished, print a message for each made sandwich

sandwich_orders = [
    'cheese and ham',
    'tuna',
    'vegan',
    'egg and onion',
    'salami',
]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nWe are preparing the {current_sandwich.title()} "
          "sandwich at the moment.")
    finished_sandwiches.append(current_sandwich)

print("\nHere is the list of finished orders:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} sandwich is ready.")
