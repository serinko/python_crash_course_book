# Loading the lowercase alphabet to a list
from string import ascii_lowercase
from random import choice

alphabet = list(ascii_lowercase)
range = list(range(1, 11))
numbers = []
for i in range:
    numbers.append(str(i))
pool = alphabet[:6] + numbers

print(
    "\n\nWELCOME TO THE LOTTERY!"
    "\nHere is a pool of 10 numbers and five letters: "
)

pool_strings_formatted = ', '.join(pool)

print(pool_strings_formatted)

print(
    "\nPlease choose a mix of 4 numbers or letters :"
)
prompt = "\nYOUR GUESS: "
prompt += "(\nprees enter after each one letter or number)\t"
guess = []
for x in range(1, 5):
    x = input(prompt)
    guess.append(x)
