# alien_0 = {
#     'color': 'green',
#     'points': 5,
# }
#
# alien_1 = {
#     'color': 'yellow',
#     'points': 10,
# }
#
# alien_2 = {
#     'color': 'red',
#     'points': 15,
# }
#
# aliens = [alien_0, alien_1, alien_2, ]
#
# for alien in aliens:
#     print(alien)


# Let's make a code generating aliens
aliens = []
# startinf with an empty list

# generate 30 green aliens
# using range tells Python how many times to loop through the loop
for alien_number in range(30):
    # run 30 times the loop in which you crade such dictionary
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    # and append it to the list of dictionaries
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created using function len()
print(f"Total number of aliens: {len(aliens)}\n")

for alien in aliens[:3]:
    # for every item in a dictionary [slice 0,1,2]:
    if alien['color'] == 'green':
        # if item[key] has this 'value'
        # change these keys to these values
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
print('\n')

# print a slice of first five dictionaries in the list
for alien in aliens[:5]:
    print(alien)
print("...")
