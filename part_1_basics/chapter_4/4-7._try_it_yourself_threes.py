	# EXCERCISE:
	# make a list of multiplies of 3 from 3 to 30
	# use for loop to print the numbers
	
threes = list(range(3,31,3))
for value in threes:
	print(value)

print("\n")
 
 # or concicesly

threes = [ value for value in range(3,31,3)]
for three in threes:
	print(three)
