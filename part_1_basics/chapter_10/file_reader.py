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
# In case my files adirectry is in the same directory as the program
# I can use A RELATIVE PATH DIRECTORY text_files/pi_digits.txt

with open(
        'text_files/pi_digits.txt'
) as file_object:
    contents = file_object.read()
print(contents)

# Or an ABSOLUTE PATH
# My text folder path is:
# /home/willow/python/python_crash_course_book/text_files
# This is not in the same folder and therefore I need to define the path
# This is called an absolute file path

with open(
        '/home/willow/python/python_crash_course_book/text_files/pi_digits.txt'
) as file_object:
    contents = file_object.read()
print(contents)

# READING LINE BY LINE
# a for loop can be used
# we start with asigning the file as a variable
# Then we can swap the string 'pi_digits.txt' with any other path
# This will then project through the entire code
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

# to eliminate the white lines:
with open(filename) as file:
    for line in file:
        print(line.rstrip())

# MAKING A LIST OF LINES FROM A FILE
# When usinh with open() is only available within the with bloc.
# If to retain an access to the content, we can store it a list
filename = 'pi_digits.txt'

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())
# the .readlines() method takes each line from the file and stores it in a list
# The list lines - can be used anytime further


# WORKING WITH A FILE's CONTENT
filename = 'pi_digits.txt'

with open(filename) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
# variable pi_string to hold the digits for pi
# a loop adds each line to pi_string + removes the newline character - rstrip()
# in the end print the string and print it's length - len()

# LARGE FILES
# Sometimes the files are lare and we can work with them,
# We can still print only a sample of it
filename = \
    '/home/willow/python/python_crash_course_book/text_files/pi_milion_decimals.txt'
with open(
        filename
) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Same method like before to make Pi into a string from the list
# The file is imported entirely. but we only print a slice (50 decimals)
# We print len() to controll the size  the content was not changed.
# Python has no limit on how much data to work with, it is about the CPU memory


# Is your birthday contained in PI
# --snip--

birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print(
        "Your birthday appears in the first milion digits of pi!"
    )
