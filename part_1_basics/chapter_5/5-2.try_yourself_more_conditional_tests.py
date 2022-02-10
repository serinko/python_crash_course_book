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
# Database for travelers
traveler_list.append('martin')
traveler_list.append('john')
traveler_list.append('barbara')
traveler_list.append('emily')
traveler_list.append('emily')
traveler_list.append('leo')
# adding registered users

client = 'ian'
# new client logged in to the application
message_logged_in = \
    "Hello " + client.title() + \
    " you are logged in to the travel application."
print(message_logged_in)
# Print welcome message to a client

print("\n")

print(client in traveler_list)
# Gives return to the system if the client is registered for the travel or not

print("\n")

# Function to compare client with the database
# Print a message for the client based on the status
if client in traveler_list:
    print("Dear " + client.title() + " we are glad you travel with us.")
else:
    print(client.title() + \
          ", we are sorry, but you are not registered for this travel.")

print("\n")

# Define admin and admin password for the application admin access
admin = 'admin'
admin_password = 'admin2022'

# Logg in input by user/admin
log_in = 'admin'
log_in_password = 'admin2022'

# Function comparing/checking for user/admin input to match with the app system
# Printing the outcome
# In case of == admin, prints the sorted list of travelers
if log_in.lower() == admin and log_in_password == admin_password:
    print( \
        "Hello, you are logged as admin. Welcome." \
        )
    print("\n")
    print( \
        "Here is the list of registered travelers for the upcoming trip:" \
        )
    for traveler in sorted(traveler_list):
        print(traveler.title())
else:
    print( \
        "Sorry, but your username and password does not match. Try again." \
        )

print("\n\n\n")

# EXCERCISE PROGRAM 3 - layers of log in:
# application for log in layers
# Define a list of comrades - with 8 comrades
# make another database mirroring the xweser comrades in the contact list
# make a variable which defines login of comrades
# make a variable which defines password for comrades
# make a variable for xweser comrades and a password for xweser comrades
# make a variable user - a field which anyone can fill and
# user password
# Print a message to the user if their name and password do not match the list
# print a message for the user if they logged in as a comrade
# Print a message if they log in as a xweser comrade
# Print a message for the system - to quickly categorize the user like:
# user comrade == True/False
# user xweser comrade == True/False

# The important point is to focus ont the first step where:
# the list_comrades and list_xweser_comrades are empty
# over time we have new users registering
# those are getting index as comrade_x or comrade_xweser_x
# the MAIN FOCUS - how do we add them to the list in the simpliest way
# without .append() every single one of them manually

list_comrades = []
list_xweser_comrades = []

# People registering as corade or xweser_comrade get a unique variable
comrade_1 = 'martin'
comrade_2 = 'mohamed'
comrade_3 = 'zu'
comrade_xweser_1 = 'sara'
comrade_xweser_2 = 'barbara'
comrade_xweser_3 = 'diana'

# BASICALLY THE GOAL IS - IN HERE - find a function where every comrade_
# and every comrade_xweser_ will be added to the list above

# WHY IS THIS NOT WORKING? :
# ~list_comrades.append(comrade*)
# ANSWER: '*' is known to PYTHON for multiplication
# a sign, function cannot be known for two different things
# thats why = only means equal and for pull if equal we use ==
# and why < ; > ; <= ; >= cant define a range bcs they are for comparisons

# Found online - do not understand the complexity of it
# Need to learn it myself
list_comrades.extend(
    value for name, value in locals().items() if name.startswith('comrade'))

list_xweser_comrades.extend(
    value for name, value in locals().items() if
    name.startswith('comrade_xweser'))

# Check up print of the lists
print(list_comrades)
print(list_xweser_comrades)

print("\n")

# DEFINED PASSWORDS
comrade_password = 'ruwsak@#ks!@'
xweser_password = 'hgcyt.,:L1W!xxrt677'

# USER INPUT
user_name = 'sara'
user_password = 'hgcyt.,:L1W!xxrt677'

# variable return_comrade = True/False if the criteria are met
return_comrade = (user_name in list_comrades
                  and user_password == comrade_password
                  or user_name in list_xweser_comrades
                  and user_password == xweser_password)

if user_name in list_comrades \
        and user_password == comrade_password \
        or user_name in list_xweser_comrades \
        and user_password == xweser_password:
    # important to define the whole comparison after 'or" function
    # not to think about it as spoken language, but define every step again
    # otherwise the function missbehave
    print("This user is registered as a comrade with a username " +
          user_name.title() + ".")

    print(">>> ")

    print(return_comrade)

if user_name in list_xweser_comrades and xweser_password == user_password:
    print("\nThis user is registered as xweser comrades with a username: " +
          user_name.title() + ".")

    print(">>> ")

    print(return_comrade)

print("\n")

# Message for the users application
if user_name in list_comrades and user_password == comrade_password:
    print("Hello " +
          user_name.title() +
          ", welcome to the application. "
          "You are registered as comrade."
          )

if user_name in list_xweser_comrades and user_password == xweser_password:
    print("Hello " +
          user_name.title() +
          ", welcome to the application. "
          "You are registered as xweser comrade."
          )

if not return_comrade:
    # the variable return_comrade is used
    # statement: if variable: means it needs value True as a return for action
    # if not variable: means that the variable value is not True (is False)
    # that the conditions were not met.
    # in this case if False (if not True)
    # the "not a correct login" message prints
    print(
        "We are sorry, but your user name and password "
        "does not match, please try again."
    )
