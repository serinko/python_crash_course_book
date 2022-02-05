players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("These are the first three players from the list:")
print(players[:3])

print("\nThese are the three players from the middle of the list:")
print(players[1:-1])

print("\nThese are the last three players from the list:")
print(players[-3:])

print("\n")

	# We can also print them not in the list form but as items
	

print("These are the first three players from the list:")
for player in players[:3]:
	print(player.title())
	
print("\nThese are the three players from the middle of the list:")
for player in players[1:-1]:
	print(player.title())

print("\nThese are the last three players from the list:")
for player in players[-3:]:
	print(player.title())
