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

avocado_list_name = list(range(1,101))
print(avocado_list_name)

print("\n")

for avocado in avocado_list_name:
	print(avocado + " avocado")
