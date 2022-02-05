	# COPYING THE LIST
	# In this case we have a list which we want to copy
	# then we define a new list as a slice of the 1st list as [:]
	
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\n My friends favorite foods are:")
print(friends_food)

	# append - can modify each list separately
	# That goes for other modyfing functions and methods
my_foods.append('cannoli')
friends_food.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)
	# prints the modified list
	# WITHOUT the 1st list modifications

print("\nMy friends favorite foods are:")
print(friends_food)
	# prints the friends lis
	# WITHOUT the my_list modifications
