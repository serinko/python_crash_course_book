
guest_list = ['vesna', 'odin', 'hecate', 'maria']
	# Defyning a list of invited people
	
	
guest_list.insert(0, 'moses')
guest_list.insert(2, 'andrei')	
	# Added gues moses on index 0 and andrei on index 2
guest_list.append('nikola')
	# Added nikola to the end of the list

print(guest_list)
	# To check the current state of the list
	
	
message_number_of_guests = "There is " + str(len(guest_list)) + \
	" guests invited to tonight's dinner."
	# Defines variable with len() function and quotes
	# len() function  counts the ammount in the list
	# str() is very important to tell Python 
	#that the number is a string, not an index
	
print(message_number_of_guests)
