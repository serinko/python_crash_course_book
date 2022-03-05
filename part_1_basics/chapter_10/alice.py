# HANDLING THE FileNotFoundError Exception

# filename = "alice.txt"
#
# with open(filename, encoding='utf-8') as f:
#     contents = f.read()

# f for file is a common convention
# encoding is an argument need to be given to an attribute in case the file
# is encoded in different format than our default sat in Python
# exception FileNotFoundError: raised because Python couldnt find the object

filename = "alice.txt"

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file  {filename} does not exist")
