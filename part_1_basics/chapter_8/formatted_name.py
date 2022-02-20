def get_formatted_name(first_name, last_name):
    """Return a full ame, neatly fortmatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# OPTIONAL ARGUMENT
# Adding an empty parameter as a default
# That can be redefined or left as it is
# if we did not defined it empty, anytime a person has no middle name..
# We recieve error
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full ame, neatly fortmatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# We got to make sure the middle name is the last parameter and argument
# if - string given == True, if not (else)== False
