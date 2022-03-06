# json MODULE
# allows you to DUMP simple Python data structures into a file
# LOAD the data from the file the next time the program runs
# It can be used to share data between different programs
# JSON is not specific to Python, it is language indenpendent

# WRITING TO JSON

import json

# import the module
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
# defining name of the filename - under which the data will be stored

with open(filename, 'w') as f:
    # Initiating a block to work with file as f ('w' for write)
    json.dump(numbers, f)
    # json.dump(VARIABLE, FILE) will save it to the file defined in filename
