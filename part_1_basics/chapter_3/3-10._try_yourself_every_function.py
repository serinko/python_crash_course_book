	# EXCERCISE POINTS
	# Make a list of your choice
	# Use every function introduced in this chaper
	
trees = ['pine', 'oak', 'ash', 'willow', 'beach', 'birch', 'fir']
trees.insert(3, 'almond')
trees.append ('hawthorn')
print(trees)

print(sorted(trees))
print(trees)

del trees[2]
print(trees)

trees[-1] = 'rowan'
print(trees)

too_exotic = 'almond'
trees.remove(too_exotic)
print(trees)
print(sorted(trees, reverse=True))
print(trees)

trees.sort()
print(trees)

trees.remove('rowan')
print(trees)

not_around = trees.pop(1)
message_not_around = "\n\nThere is no " + not_around.title() + " around here.\n\n"
print(message_not_around)

print(trees)
trees.reverse()
print(trees)

trees.append('apple')
print(trees)
trees.sort()
print(trees)

print("\n")
message_trees_count = "There is " + str(len(trees)) + " trees in the list at the moment."

message_list_state = "\n\n" + message_trees_count + "\nThe current and aphabetically sorted version of the list looks like this:\n" + str(sorted(trees)) + ". \nWhere the " + str(trees[0]).title() + " tree is the first one, and the " + str(trees[-1]).title() + " tree is the last one in the list."
print(message_list_state)

trees.append('birch')
trees.remove('apple')
trees[0] = 'maple'
trees.insert(3, 'cypres')
trees.sort()

message_trees_count = "There is " + str(len(trees)) + " trees in the list at the moment."
message_list_state = "\n\n" + message_trees_count + "\nThe current and aphabetically sorted version of the list looks like this:\n" + str(sorted(trees)) + ". \nWhere the " + str(trees[0]).title() + " tree is the first one, and the " + str(trees[-1]).title() + " tree is the last one in the list."
print(message_list_state)


