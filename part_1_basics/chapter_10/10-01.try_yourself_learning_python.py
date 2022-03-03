filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

print("\n\n")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("\n\n")

with open(filename) as file_object:
    lines = file_object.readlines()

learning_python_string = ''

for line in lines:
    learning_python_string += line.rstrip()

print(learning_python_string)