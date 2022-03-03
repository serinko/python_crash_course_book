filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learning_python_string = ''

for line in lines:
    line.replace('code', 'anarchist phillosophy')
    learning_python_string += line

learning_python_string.replace('code', 'anarchist phillosophy')

print(learning_python_string)

print("\n\n")
