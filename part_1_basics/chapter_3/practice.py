message_introduction = "Please write down your favourite colors.\n"
	# This is an intdoctudion message
	# \n in the end makes a spacing under the sentence - free line
print(message_introduction)
	# This will print it for the reader
	
favorite_colors = []
	# Start with empty list, whih will be filled by the user
	
message_2 = "My favourite colors are:"
print(message_2)
	# Marks the input by the user
favorite_colors.append('grey')
favorite_colors.append('green')
favorite_colors.append('purple')
	# favorite_colors added by user with a function to add to the list



print(favorite_colors[0] + ', ' + favorite_colors[1] + ', ' + favorite_colors[2])
	# Picked the colors from the list to print them for the user
	# Be aware of spelling - favourite doesn't = favorite

print("\n")
	# adds a space
	
index_1 = 0
		# To change index instead of a variable in each sentence
	
message_describe_colors = 'Please describe why each of those are your favorite colors in a sentence.\n'
	# ask to write one sentence to descibe the colors in the list
	
print(message_describe_colors)
	# print the message
	
message_1 = 'When it comes to my style, I would chose ' + favorite_colors[0] + ' as my number one to wear.\n'
	# Makes a color chosen from the list to be chosen for clothes

message_2 = favorite_colors[1].title() + ' is my favorite one, when it comes to every day surounding.\n'
	# .title() function added to make the color starting with a capitol letter

message_3 = favorite_colors[2].title() + ' is more generally nice, just like a color I like a lot.\n'
	# same .title() using 3rd item - [2]
	
print(message_1)
print(message_2)
print(message_3)
	# Prints the messages
	
