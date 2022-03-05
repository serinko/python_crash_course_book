# HANDLING THE FileNotFoundError Exception

# filename = "alice.txt"
#
# with open(filename, encoding='utf-8') as f:
#     contents = f.read()

# f for file is a common convention
# encoding is an argument need to be given to an attribute in case the file
# is encoded in different format than our default sat in Python
# exception FileNotFoundError: raised because Python couldnt find the object

filename = "Alice in Wonderland.txt"

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file  {filename} does not exist")
    # This prevents the error from stopping the code
    # Else block will define what do do the try text was successfull
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# We create string called contents
# use split() method to split it into words and store them in a list words
# len() method counts object(words) in that list
# We print the count
# All this code is placed in the else bloc, as it will work only when the file
# exists in the given directory

