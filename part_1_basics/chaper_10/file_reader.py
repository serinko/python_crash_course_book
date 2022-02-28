# READING FROM A FILE

# 1) READING AN ENTIRE FILE:
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# The first line: open() accesses the file
# argument - needs the name of the file to open
# It looks in the directory where the program is stored
# returns an object representing the file
# asigns it to the file object variable

