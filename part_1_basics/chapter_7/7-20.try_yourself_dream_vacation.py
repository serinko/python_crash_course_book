# EXCERCISE
# Write a program that polls users into their dream vacation
# Make a prompt to ask users where they like to go
# make block of code printing the entir
dream_vacation = {}
passwords = []
active = True

print("\nHello and welcome to the poll of favorite vacation.\n")
while active:
    name = input("\nWhat is your name? ")
    vacation = input("\nWrite a place you really like to visit: ")
    password = input("Enter your password: ")

    dream_vacation[name] = vacation

    print("\nThank you for your input, your answer was submited.")
    print("\nWe will release the poll once everyone submits.")

    more_users = input("\nAnother person would like to join the poll?"
                       "(yes/ no)")

    if more_users.lower() == 'no':
        active = False

print("\nAll the users submited, the poll is closed")

name_check = input("\nTo see the results, you must log in. Please, enter your "
                   "name: ")
password_check = ("\nPlease enter your password: ")

if name_check in dream_vacation.keys() and password_check in passwords:
    print(f"\nHey {name_check.title()}, welcome to the vacation poll. "
          f"\nHere are the results: ")
    print("\n\n\n   ----------- POLL RESULTS -----------   \n")

    for name, vacation in dream_vacation.items():
        print(f"{name.title()}'s vacation of their dreams is "
              f"{vacation.title()}.")

else:
    print("\nWe are sorry, but your name and password does not match."
          "\nFor more information visit www.lifeis.struggle.")