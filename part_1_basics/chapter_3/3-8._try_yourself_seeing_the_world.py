	# EXCERCISE POINTS
	# Think of five places you want to see
	# Store them in a list not sorted
	# Print it raw as it is
	# use sorted() to print it without modifying the order
	# Show that your list is still in the original order
	# use sorted() to print it in an alphabetically reversed order
	# show that the list is still in an original order
	# use reverse() to chane the order of your list
	# use the reverse() agao and show it is in original order again
	# use sort() to sort the list in alphabetical order permanently
	# use sort() to sort your list in an alphabeticaly reversed order


locations_to_see = ['chiapas', 'bajkal', 'sarek', 'sumava', 'bakur']
print("These are some of the locations I would like to visit")
print(locations_to_see)

print(sorted(locations_to_see))

print(locations_to_see)

print(sorted(locations_to_see, reverse=True))

print(locations_to_see)

locations_to_see.reverse()
print(locations_to_see)

locations_to_see.reverse()
print(locations_to_see)

locations_to_see.sort()
print(locations_to_see)

locations_to_see.sort(reverse=True)
print(locations_to_see)



