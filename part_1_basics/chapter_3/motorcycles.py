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
	
print(motorcycles)

motorcycles[0] = 'hurley'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.append('scooter')
print(motorcycles)

motorcycles[-1] = 'vespa'
print(motorcycles)

del motorcycles [-1]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
	#introducing the new method pop()
	# pop() takes an item from the end of the list but keeps it's value
	# by this we stored the value of pop() item in a variable popped_motorcycles
print(motorcycles)
	# Shows a list without the popped - last item
print(popped_motorcycles)
	# print the value of the removed item from the list
	# popped_motorcycles was defined by me as a variable
	
print(popped_motorcycles.title())
	# prints the popped item with the title() method
	
	
	# This method can be used to restore something from chronological order:
motorcycles = ['honda', 'yamaha', 'suzuki']
	# Defining new list of motorcycles - 3 I have owned
last_owned = motorcycles.pop()
	# Defining a variable of ast owned from the end of the chronologicla list
print("The last owned motorcycles of me was a " + last_owned.title() + ".")








