# Nesting dictionary as a value into each key of a dictionary

users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# in a for loop we have key, value in the dictionary
# we print the key as a username
# The value we know is another dictionary
# define full name as a value=inner_dictionary[key] ('first') and
# value_is_inner_dictionary[key] ('last)
# the same with the location
# then we simply print these
# Note that these were identicaly structured dictionaries
# In case they were different - the code in for loop d be more complicated
