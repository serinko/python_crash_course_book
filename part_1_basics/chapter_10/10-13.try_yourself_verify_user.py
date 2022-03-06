import json


def get_stored_username():
    """Get stored username if available"""

    filename = 'user.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:

        return username


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


# def username_content():
#     filename = 'user.json'
#     try:
#         with open(filename) as f:
#             content = f.read(json.load(f))
#
#         return content
#
#     except json.decoder.JSONDecodeError:
#         return None


def check_user():
    username = get_stored_username()
    message = f"Hello. Are you user {username}?"
    print(message)
    prompt = "\nEnter 'yes' or 'no':   "
    answer = input(prompt)

    if answer == 'yes':
        print(f"Welcome back {username}.")

    elif answer == 'no':
        username = input("Enter your actuall username:   ")
        print(f"You are signed in as {username}.")
        filename = 'user.json'
        with open(filename, 'w') as f:
            json.dump(username, f)


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    # username_content = username_content()

    if username:
        check_user()

        # try:
        #     get_stored_username()
        # except json.decoder.JSONDecodeError:
        #     username = get_new_username()
        #     message = f"We'll remember you when you come back, {username}!"
        #     print(message)
        #
        # else:
        #     f"Welcome back, {username}!"





    else:
        username = get_new_username()
        message = f"We'll remember you when you come back, {username}!"
        print(message)


greet_user()

# new function get_stored_username
