
guest_list = ['vesna', 'odin', 'hecate', 'maria']
	# Defyning a list of invited people
guest_index = guest_list[0]
	# Defyning the guet from the list according their index
	# Making a variable esy to eaxchange further on
message_invitation = "Dear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
	# invitation message as a variable with the index variable
	# Adding title() method for a correct grammar of the name.
print(message_invitation)
	# printing the invitation message, index 0 + title() = Vesna
	
	# REPEAT FOR OTHER GUESTS

guest_index = guest_list[1]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)


guest_index = guest_list[2]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)


guest_index = guest_list[3]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

print("\n")

	# ODIN CANNOT COME!
	# print that statement
	# Invite an extra person
	# Change the list accodingly
	# Print invite message for everyone in the list
	
	
cannot_come = guest_list.pop(1)
	# Defyning that index 1 = odin, cannot come as a variable
	# using pop(function)
message_cannot_come = "Dear guests, I would like to inform you, that " + cannot_come.title() + " will not be able to join us today."
	# message is defined including the variable cannt_come
print(message_cannot_come)
	# printing message to the guest's informing that one cannot_come
	
guest_list.append ('diana')
	 # adds a new guest diana in the end of the guest list
	 
	 # PRINT AN VITATION MESSAGE TO EVERYONE IN THE LIST
	 
guest_index = guest_list[0]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

guest_index = guest_list[1]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)


guest_index = guest_list[2]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)


guest_index = guest_list[3]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

	
	# MORE SPACES ON THE TABLE
	# Inform all the guests that there are more seats available
	# use insert() to add more ppl to the list
	# use append to add more ppl to the list
	# print a new invitation message to everyone in the list
	
message_more_seats = "\nDear guests, I found a bigger table, so more people will be invited to today's dinner. The invitations will be printed for everyone in few minutes."
	# Defining variable with the message about more seats
print(message_more_seats)
	# Printing that message
	
	
