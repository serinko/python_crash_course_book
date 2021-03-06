filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learning_python_string = ''

for line in lines:
    line.replace('code', 'anarchist phillosophy')
    line = line.replace('code', 'anarchist philosophy')
    learning_python_string += line

    # method replace() could also be done through following syntax:
    # learning_python_string = learning_python_string.replace(
    #    'code', 'anarchist philosophy'
    # )

# Or we with this syntax:
# learning_python_string = learning_python_string.replace(...)
# or alternatively - to keep the original intact and use a copy
#  of the text with replace() method only for the print:
# print(learning_python_string.replace(...)) - in case we havent changed it yet
print(learning_python_string)

# print(learning_python_string.replace('code', 'anarchist philosophy'))

print("\n\n")
