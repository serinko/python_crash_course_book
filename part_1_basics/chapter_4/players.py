players = ['charles', 'martina', 'michael', 'florence', 'eli']
	# defnes a list of "players"
print(players[0:3])
	# Same like when defining an item, we used "slice"
	# this defines a group of items from the list
	# when range is (,) slice uses [:]
	# as in range the frs tindex is where the range starts
	# the last marks the border, so the slice prints -1 from it
	# because list counts from 0, do nt forget off-by-one rule
print(players[1:4])
	# prints a slice with indexes 1,2,3
	
print(players[:2])
	# Pythond utomatically starts at the begnning of the list

print(players[2:])
	# similar syntax - Python slices from "2" till the end
	
print(players[-3:])
	# the negative ndex counts from the end
	# this will outtput a slie 3 items from the end
	# we didnt define the second index, it prints till the end
	
	
	# for LOOP AND SLICE
print("Here are the frst three players of my team:")
	# prints a sentence for all
for player in players[:3]:
	# defines a variable player and = an item in the list of players
	# at the same time defines the slice of the list to loop in
	# by using the [] method
	print(player.title())
	# prints each item in the given slice
	# with .title() method
