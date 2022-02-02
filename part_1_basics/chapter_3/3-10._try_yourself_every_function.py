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

