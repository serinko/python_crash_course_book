current_users = ['admin', 'francesca', 'eva', 'ivan', 'rick', 'mellisa']
new_users = ['clemence', 'EVA', 'ivan', 'emily', 'steve', 'mellisa']

if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print(
                "This user name is already taken, "
                "pick another one, please."
            )
        else:
            print(
                "Hello, you have created an account with a username " +
                user.title() + "."
            )
        print("\n")

else:
    print("The space for username must be filled to register.")
