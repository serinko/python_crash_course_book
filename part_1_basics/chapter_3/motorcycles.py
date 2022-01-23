motorcycles = ['honda', 'yamaha', 'suzuki',]
	# List of motorcycles, honda in position 0 is the first element
print(motorcycles)

motorcycles[0] = 'ducati'
	# it changes the value of the first item to ducati
	# the rest of the list remains
print(motorcycles)

motorcycles.append('hurley')
	# .append adds 'hurley' to the end of the list 
	# without any impact on the order of the list
print(motorcycles)

motorcycles = []
	# Creates an empty list motorcycles
motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('suzuki')
	# adds items to the empty list
print(motorcycles)
	# This is a usual way to do it - start with am epty list
	# you do not know what value users will entry later 
	# But you cannot wait to program it after you have all the value
	# Values will be constantly changing
	
del motorcycles[0]
	# del statement removes an item from the list based on it's position
	# meaning the del motorcycles[0] takes away the first one = 'honda'
print(motorcycles)

del motorcycles[1]
	# you can use this with any item as long as you know it's index
	# [1] will remove the second one in the list, which is now 'suzuki'
print(motorcycles)
	# That means that you can no longer access the value in the list
	
motorcycles =  ['honda', 'yamaha', 'suzuki',]
	# Defyning new list of motorcycles
	
print(motorcycles[0])
	# prints 1st item from the list
print(motorcycles[-2])
	# prints second one fromt the end
	# BEWARE the diffrence 1st is [0] but last is [-1]!
	

