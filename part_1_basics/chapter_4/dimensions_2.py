dimensions = (200,50)
	# TUPLE is a list of immutable items
	# That means that they cannt be changed
	# defined as a list with () instead of []
print("Here are the dimesions:\n")

	# you can loop through values in a tuple
for dimension in dimensions:
	print(dimension)

dimensions = (220,75)
print("\nHere are the re-defined dimensions:")
for dimension in dimensions:
	print(dimension)

	# compared t a list 
	# tuples are simple data structure
	# use them if you want to have values which will not hange through
	# the life of the program
