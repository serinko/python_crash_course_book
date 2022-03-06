import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        number = json.load(f)

except FileNotFoundError:
    prompt = "What is your favourite number?\n\n"
    number = input(prompt)
    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f"Number {number} was stored as your favorite number.")

else:
    print(f"Your favorite number is {number}.")
