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
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             content = f.read(json.load(f))
#
#         return content
#
#     except json.decoder.JSONDecodeError:
#         return None


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    # username_content = username_content()

    if username:
        prompt = "Enter your username:  "
        user = input(prompt)
        if user == username:
            print(f"Welcome back, {username}!")
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
            message = "We are sorry but you are not the registered user."
            print(message)




    else:
        username = get_new_username()
        message = f"We'll remember you when you come back, {username}!"
        print(message)


greet_user()

# new function get_stored_username
