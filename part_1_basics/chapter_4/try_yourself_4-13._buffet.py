	# EXCERCISE:
	# A buffet offer only 5 very simple dishes
	# make such list and store them in  tuple
	# use a for loop to print each dish the restaurant offers
	# Try to modify one and see what Python does
	# Two dishes change - write a block of code to redefine the tuple
	# print it through for loop function
	
buffet_menu = ('hummus', 'cheese spread', 'guacamole', \
'pita bread', 'nachos')

print("The buffet menu:")
for food in buffet_menu:
	print(food.title())
	
buffet_menu[2] = 'bacon toast'
buffet_menu[-1] = 'hash browns'


print("The buffet menu:")
for food in buffet_menu:
	print(food.title())
