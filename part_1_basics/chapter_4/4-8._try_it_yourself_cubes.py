	# EXCERCISE:
	# A number raised to the third power is calle dcube
	# ie the cube of 2 is expressed as 2**3
	# Make the list of the frst 10 cubes in (cube for each integer 1-10)
	# use for loop to print value of each
	
cubes = [value**3 for value in range(1,11)]
	# defining the list cubes, using LIST COMPREHENSION method
	# using the variable value**3 loping for each step in the range
	
for cube in cubes:
	# for loop with a variable cube and list of cubes
	print(cube)
	# finally printing it
