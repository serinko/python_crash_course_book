def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein,',
                             location='princeton', field='physics')

print(user_profile)

# **parameter tells Python to create a dictionary with such name
# The two positional parameters, which we defined as keyword in the dictionary
# The rest is arbitrary, added as arguments in the variable user_profile
