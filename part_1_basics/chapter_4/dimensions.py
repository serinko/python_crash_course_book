dimensions = (200,50)
	# TUPLE is a list of immutable items
	# That means that they cannt be changed
	# defined as a list with () instead of []
print(dimensions[0])
print(dimensions[1])
	# just printing it's items like in the list
	
dimensions[0] = 250
	# This is not working because tuple cannot be altered
	# The values defined in dimensions must stay the same
	# unles the whole tuple is not re-defined
print(dimensions[0])
	# we get an error message
