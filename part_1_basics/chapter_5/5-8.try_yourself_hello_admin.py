# ~ list_users = ['admin', 'francesca', 'eva', 'ivan']
list_users = []

if list_users:
    for user in list_users:
        if user == 'admin':
            print(
                'Hello ' + user.title() +
                ', you are logged in, would you like to see a status report?'
            )
        else:
            print(
                'Hello ' + user.title() +
                ', you are successfully logged in. Welcome.'
            )
else:
    print("We need to find users for this application")
