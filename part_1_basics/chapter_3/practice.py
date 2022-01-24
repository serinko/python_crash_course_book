message_introduction = "Please write down your favourite colors.\n"
	# This is an intdoctudion message
print(message_introduction)
	# This will print it for the reader
	
favorite_colors = []
	# Start with empty list, whih will be filled by the user
	
message_2 = "My favourite colors are:"
print(message_2)
	# Marks the input by the user
favorite_colors.append('black')
favorite_colors.append('green')
favorite_colors.append('turcois')
	# favorite_colors added by user with a function to add to the list

print(favorite_colors[0] + ', ' + favorite_colors[1] + ', ' + favorite_colors[2])
	# Picked the colors from the list to print them for the user
	# Be aware of spelling favourite doesn't = favorite
