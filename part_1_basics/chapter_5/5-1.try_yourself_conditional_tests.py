# EXCERCISE:
# Write a series od conditional tests
# print a statement describing each test and your precondition for the result
# Look closely at the results
# make sure you understand why each line evaluates True or False
# Create 10 such tests. 5 True and 5 False

car = 'subaru'
print("Is car == 'subaru'?  I predict True.")
print(car == 'subaru')
# important detail - the print has no quotation but uses == as a\
# variable comparison - so the print will be True or False

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\n")

number = 1
print("Is number >= 0? I predict True")
print(number >= 0)
# Here we used a numeric comparison, where value in the variable = 1
# And the prediction is tha the number is >= 0
# We get True
print("\n")

user_0_number = 1
print("I believe the number is " + str(user_0_number) + ".")
print(number == user_0_number)
# here we have a comparison, where the user number is 1 as ell as number is 1
# We added user numer to the first sentence
# print is a == comparison in between te number and user_number
# So the print is True
print("\n")

user_1_number = 5
print("The I believe the number == " + str(user_1_number) + ".")
print(user_1_number == number)
# user_1 guessed the number 5. Prints False.
print("\n")

user_2_number = range(1, 100)
user_3_number = range(4, 100)
# We added ranges as a solution to the problem when:
# comparing < > signs cannot be use for definition.

print("If user 1 and user 2 are right, print True")
print(user_2_number and user_3_number == number)
# Here we using and as a function - both must be True to == True
print("\n")

print("If either user 1 or user 2 are right, print True")
print(user_2_number or user_3_number == number)
print("\n")

print("If either user 1 or user 2 are right, print True")
if user_2_number or user_3_number == number:
    print(True)
print("\n")

print("If either user 1 or user 2 are right, print True")
if user_2_number or user_3_number == number:
    print('True')
# Keeping the same users (2 and 3) but the function is OR so either is enough
# for the return True
print("\n")
