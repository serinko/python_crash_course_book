# EXCERCISE:
# MAKE MORE COMPARISONS AND TESTS
# Get some True and False results for following:
# test for equality and inequality with strings
# test using the lower() function
# Numerical tests with ==;!=;<;>;<=;>=
# using the and and or function with a keyword
# Testing whether ite is in the list
# Testing whether an item is not in the list

# PROGRAM 1 - Lottery: there is a number of the day and users can guess
# user number gets compared with the number of the day and prints message back
number = 38
# The number of the day

user = 'matias'
# Players name saved in a variable user
users_number = 23
# Players guess

# A function compares users_number with the number of the day
# and prints an answer
if users_number == number:
    print("Dear " + user.title() + ", you are a winner of our lottery. \
    Congratulation!")
else:
    print("Dear " + user.title() + ", we are sorry, but this is not " \
                                   "the number. Do you want to try again?")
# users guess was wrong
print("\n")

user = 'lilly'
# New player - variable was redefined
users_number = 38
# Guess number was redefined accoring to a new users guess
if users_number == number:
    print("Dear " + user.title() + ", you are a winner of our lottery. " \
                                   "Congratulation!")
else:
    print("Dear " + user.title() + ", we are sorry, but this is not " \
                                   "the number. Do you want to try again?")
# This player won

print("\n\n")

# PROGRAM 2 - Make a database of travelers
# add registered clients to the list of travelers
# when a client logs in to the application, give a return
# a) print a "successfully logged in" message
# b) for the program to compare if client is registered for travel or not
# c) print a message for the client if registered
# If admin logs in with a correct password:
# a) print them a welcome admin message
# b) print a list of travelers, alphabetically sorted

traveler_list = []
traveler_list.append('martin')
traveler_list.append('john')
traveler_list.append('barbara')
traveler_list.append('emily')
traveler_list.append('emily')
traveler_list.append('leo')

client = 'ian'
message_logged_in = \
    "Hello " + client.title() + \
    " you are logged in to the travel application."
print(message_logged_in)

print("\n")

print(client in traveler_list)

print("\n")

if client in traveler_list:
    print("Dear " + client.title() + " we are glad you travel with us.")
else:
    print(client.title() + \
          ", we are sorry, but you are not registered for this travel.")

print("\n")

admin = 'admin'
admin_password = 'admin2022'

log_in = 'Admin'
log_in_password = 'admin2022'

if log_in.lower() == admin and log_in_password == admin_password:
    print( \
        "Hello, you are logged as admin. Welcome." \
        )
    print("\n")
    print( \
        "Here is the list of registered travelers for the upcoming trip:" \
        )
    for traveler in list_of_travelers:
        print(traveler.title())
else:
    print( \
        "Sorry, but your username and password does not match. Try again." \
        )

print("\n")
