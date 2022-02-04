magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)
	# for is a loop function
	# firt time I can see that I used a function print in moved under another function 
	# for ITEM in LIST_OF_ITEMS
	# singular and plural helps to navigate if we talk about the list or variable
	print("\n")

for magician in sorted(magicians):
	print(magician.title())
	# This prints each item in sorted() order
	# with the tittle() function
	# I want to make a note which has several informations such as
	
print("\n")	
for magician in magicians:
print(magician.title() + ", that was a great trick.")
	# prints a message to each of the item (magician) in the list (magicians)
	print("I cannot wait to see your performance, " + magician.title() + ".\n")
	# prints a message to each with a space in between ech message

print("Thank you everyone, this was an amazing show")
	# Prints one message only, it is not part of the for loop
	
	# INDENTING IS IMPORTANT
	# Make sure you indent correctly
	# and opposie that you do not indent what is not suppose to be

prnt(magicians)
