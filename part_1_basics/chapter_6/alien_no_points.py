# Using get() to access value
alien_0 = {
    'color': 'green',
    'speed': 'slow',
}

# print value, which is not defined
# ~ print(alien_0['points'])
# gives KeyError: 'points'

# get() method
point_value = alien_0.get('points', 'No point value asigned.')
print(point_value)
# If the key 'points' exists - we get the corresponding value
# if does not exist, we get the 'default' value
# message gets printed clean without any error

# If there is a chance the key you are asking for has no value
# consider using get() method
