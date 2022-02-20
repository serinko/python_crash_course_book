# RETURNING A DICTIONARY
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name,
    }
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# This way makes our data stored in parameter as well as in dictionary
# we can then easily modify for optional return

def build_person(first_name, last_name, age=None):
    # in case of numbers we dont define empty string but None as a default
    # In conditional tests None == False, it is a placeholder
    """Return a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name,
    }
    if age:
        person['age'] = age
    # if age is given == True:
    # dictionary person will add a key 'age' with the value of age
    return person


musician = build_person('jimi', 'hendrix', age=27)
# We defining parameter and argument age=27
print(musician)
