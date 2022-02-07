banned_users = ['andrew', 'carolina', 'david']
# List of values - banned users
user = 'marie'
# A new variable; user = marie

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# variable user is compared with the list
# if it is NOT there - the message prints
