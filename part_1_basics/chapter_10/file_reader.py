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
# 'with' closes the file once the access is no longer needed

# We do not use close() here. - if a bug would disturb -
# the program - it may never close
# That may cause data to be lost or corrupted.
# and if you close too early, you may we working with a closed file
# one you cannot access
# read() method reads the content and stores it in a string (contents)
# Python closes the file automatically when the block finishes execution.

# There is an extra blank line, if we want to remove it, use rstrip()
print(contents.rstrip())

# Output than matches the originall file

# 2) FILE PATHS:
with open(
        '/home/willow/python/python_crash_course_book/text_files/pi_digits.txt'
) as file_object:
    contents = file_object.read()
print(contents)
# My text folder path is:
# /home/willow/python/python_crash_course_book/text_files
