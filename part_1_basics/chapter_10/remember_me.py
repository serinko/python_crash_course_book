# SAVING AND READING USER-GENERATED DATA

# import json

# Load the user data if it as been stored previously
# Otherwise prompt for the username and store it

# filename = 'username.json'
#
# try:
#     with open(filename) as f:
#         username = json.load(f)
#
# except FileNotFoundError:
#     username = input("What's your name? ")
#
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}!")
#
# else:
#     print(f"Welcome back, {username}!")


# REFACTORING - BREAKING INTO FUNCTIONS

import json


def get_stored_username():
    """Get stored username if available"""

    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:

        return username

    # This block try-except tests if filename exists and returns the value
    # if it does not - The value is None


def get_new_username():
    """Prompt for a new username"""
    prompt = "Hello, please enter your username:  "
    username = input(prompt)
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
    # This function prompts new user name and gets called for by
    # greet_user only if the stored_user_name does not exist


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        try:
            get_stored_username()
        except json.decoder.JSONDecodeError:
            username = get_new_username()
            message = f"We'll remember you when you come back, {username}!"
            print(message)

        else:
            f"Welcome back, {username}!"




    else:
        username = get_new_username()
        message = f"We'll remember you when you come back, {username}!"
        print(message)


greet_user()

# new function get_stored_username
