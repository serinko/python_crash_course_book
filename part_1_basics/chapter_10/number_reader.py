# READING FROM JASON

import json

# import the module

filename = 'numbers.json'
# defining name of the filename - name of file from data will be loaded

with open(filename) as f:
    numbers = json.load(f)
    # efyning the name of the variable (list) for the data in json

print(numbers[0])
# reading item with index [0] from the list and prints

print(numbers)
# prints the whole list
