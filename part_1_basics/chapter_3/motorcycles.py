motorcycles = ['honda', 'yamaha', 'suzuki',]
	# List of motorcycles, honda in position 0 is the first element
print(motorcycles)

motorcycles[0] = 'ducati'
	# it changes the value of the first item to ducati, the resto of the list remains
print(motorcycles)

motorcycles.append('hurley')
	# .append adds 'hurley' to the end of the list without any impact on the order of the list
print(motorcycles)

motorcycles = []
	# Creates an empty list motorcycles
motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('suzuki')
	# adds items to the empty list
print(motorcycles)
