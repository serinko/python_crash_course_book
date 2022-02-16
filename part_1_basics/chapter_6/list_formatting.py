# LIST FORMATTING
# In this chapter we faced the question:
# How to format a list if one does not want to pint it eithe:
# [as, a, list] or:
# in a for loop
# There are several methods, as well as different applications in case:
# a) list contains strings
# b) list contains numbers

# a) LIST OF STRINGS
list_strings = ['a', 'b', 'c', ]

# straight on printing the list
print(list_strings)

# using for loop statement
for string in list_strings:
    print(string)

# if we want to print the list in one line, without the [] list formatting
# method .join()

list_strings_formatted_1 = ", ".join(list_strings)
# first create a variable, which is defined as:
# a "parameter_in_between".join(original_list)
# The parameter in between can be anything. Let's print few examples:
# (you print the new variable - not the original list)
print(list_strings_formatted_1)

list_strings_formatted_2 = "--".join(list_strings)
print(list_strings_formatted_2)

list_strings_formatted_3 = " .. anything you choose .. ".join(list_strings)
print(list_strings_formatted_3)

# alternatively, I found:
# function end. It works but was hard to  implement in a longer f-string
# To use end, we need to loop through list
# and add ,end="parameter_in_the_end" only when printing the original list
# ie print(list, end=",")
# example may be self-explanatory
for a in list_strings:
    print(a, end=", ")
    # The result - as the function suggest
    # prints the parameter after each string
    # if we did not use for loop:
    # ,end=... would only come after the entire list
print("\n")

# again, any parameter can be used
for a in list_strings:
    print(a, end=" ## ")
print("\n")

# Sometimes we may want to have ie commas just in between.
# besides .join(), we can use ,sep="parameter_in_between"
# Function ,sep does not need a for loop
# but we use the * sign before the name of printed list
# example:
print(*list_strings, sep=", ..sep_method.. ")
# We see that sep parameter is printed only in between (separates)
# if we did not use * sign, it would sep the entire list
print("\n\n")

# b) LIST OF NUMBERS
list_of_numbers = list(range(1, 10))
print(list_of_numbers)
# Classic print, nothing unexpected

for number in list_of_numbers:
    print(number)
# classic for loop print

# the method .join works well, but:
# numbers must be formatted into strings, otherwise we will get an error
# We create another variable/list, where we save the numbers in string format:
numbers_strings = [str(n) for n in list_of_numbers]
# you can check - what comes out:
print(numbers_strings)
# to geth the numbers printed behind each other in one line,
# we can now just use any of the methods presented in a)
# because numbers are just strings.
# example:
numbers_strings_formatted_1 = ", ".join(numbers_strings)
numbers_strings_formatted_2 = "--".join(numbers_strings)
numbers_strings_formatted_3 = \
    " .. anything you choose .. ".join(numbers_strings)

print(numbers_strings_formatted_1)
print(numbers_strings_formatted_2)
print(numbers_strings_formatted_3)

# same can be implemented with ,end= and ,sep= functions
