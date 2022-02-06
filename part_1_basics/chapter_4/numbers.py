for value in range(1,5):
	print(value)
	# Pythn stops on the second value
	# by the time it hits 5, it stops
	# so there is the same problem with off-by-one
print("\n")

for value in range(1,6):
	print(value)
	# if you want to print 1-5, the range must be 1,6
	
print("\n")

numbers = list(range(1,6))
print(numbers)

print("\n")

avocado_list_name = list(range(1,11))
	# IMPORTANT - This is how to create a list
print(avocado_list_name)
	# comes out as a list

print("\n")

for avocado in avocado_list_name:
	print(avocado)
	# the variable can have whatever name
	# as long as we refer to the for NAME 
	
print("\n")

for poop in avocado_list_name:
	print(str(poop) + " avocado")
	# if we print simple range numbers str() not needed
	# if we use ITEM which is not a number +  quote, str() also not needed
	# if ITEM (poop) translates into a digit and adding a quote, 
	#str() is a must

print("\n")

list_1_0 = list(range(1,0))
print(list_1_0)
	# Prints an empty list as there is no range between 1 and 0

print("\n")
	
list_7_0 = list(range(7,0))
print(list_7_0)
	# Range only works upwards - list comes empty if printed in range 7 - 0

