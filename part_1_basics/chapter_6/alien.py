# dictionary{key:value}
alien_0 = {'color': 'green', 'points': 5}
# alien_0 is a dictionary
# {} define the key and connected values in the dictionary

print(alien_0['color'])
print(alien_0['points'])
# print(dictionary['key'])
# this will print the value of the key in the given dictionary
# key value can be: a number, string, list, another dictionary - any object
# dictionary = {key:value} or multiple {key_0:value_0, key_1:value_1}
# "function/call(dictionary[key])" returns: "value"

# using the values in the dictionary to store in new variables, strings etc
new_points = alien_0['points']
# associates value of the key point of dictionary alien_0 to a variable

print("You just earned " + str(new_points) + " points!")

print("\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
# adding to the database alien_0[key] = value
print(alien_0)

print("\n")

# MODIFYING THE VALUES
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ".")

print("\n")

# LET'S BE DYNAMIC
# We can move the alien

alien_0['speed'] = 'medium'
print(
    "Original x-position: " + str(alien_0['x_position'])
)
# ~ print(alien_0)


# Let's move the  alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This is a fast moving alien
    x_increment = 3

# With this statement we have a variable x_increment
# Its changes based on the defined speed
# Speed is also stored in the dictionary alien_0
# Can be modified by dictionary modyfication

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(
    "New x-position: " +
    str(alien_0['x_position'])
)

# New move - this time fast
# Chane the speed in the dictionary and run again the sequnce
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This is a fast moving alien
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(
    "New x-position: " +
    str(alien_0['x_position'])
)

print("\n")

# DELETING key from a dictionary
# using del statement
# del dictionary['key']

print(alien_0)

del alien_0['points']

print(alien_0)
