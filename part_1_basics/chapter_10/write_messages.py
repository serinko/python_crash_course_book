# WRITING TO A FILE

filename = 'programming.txt'

with open(filename, 'w') as text_file:
    text_file.write("I love programming.\n")

    # 'w' is for write mode
    # the open() function creates the file if it did not already exist
    # BE CAREFUL !!! - if the file does exist - it will be erased and replaced
    # Python only write strings to a text file. Numbers must be str() formatted.

    # WRITING MULTIPLE LINES
    # with open(filename, 'w') as text_file:
    #     text_file.write("I love programming.")
    text_file.write("I love creating new games.\n")

# APPENDING TO A FILE
# Python does not erase but append to a file
# We can modify a textfile like this:
with open(filename, 'a') as text_file:
    text_file.write("I also love finding meaning in large databases\n")
    text_file.write("I love creating apps that help every day life\n")
