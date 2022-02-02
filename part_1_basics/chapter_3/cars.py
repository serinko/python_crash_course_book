cars = ['bmw','audi','toyota','subaru']
cars.sort()
	# Method sort() made the list sorted alphabetically
	# This change is PREMANENT! 
print(cars)

print("\n")

cars.sort(reverse=True)
	# Reverse the order backward
	# Again stays permanent
print(cars)

print("\n")

cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
	# Adding sorted() where cars are in ()
	# This displays the list sorted alphabethically
	
print("\n")

print("\nHere is the original list again:")
print(cars)
	# Without changng anything on the list, it prints as the original

print(sorted(cars, reverse=True))
	# This displays reverse order
	# It is temporarily - the list still stays

print("\n")

cars.reverse()
	# Reverse the order of the list
	# Does not sort, but REVERSE
print(cars)
