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
