# json MODULE
# allows you to DUMP simple Python data structures into a file
# LOAD the data from the file the next time the program runs
# It can be used to share data between differen programs
# JSON is not specific to Python, it is language indenpendent

# WRITING TO JSON

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
