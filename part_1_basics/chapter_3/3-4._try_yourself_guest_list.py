guest_list = ['vesna', 'odin', 'hecate', 'maria']
	# Defyning a list of invited people
guest_index = guest_list[0]
	# Defyning the guet from the list according their index
	# Making a variable esy to eaxchange further on
message_invitation = "Dear " + guest_index.title() + " I would like to invite you for a dinner at my place, tonight. Hope to see you there."
	# invitation message as a variable with the index variable
	# Adding title() method for a correct grammar of the name.
print(message_invitation)
	# printing the invitation message, index 0 + title() = Vesna
	
	# REPEAT FOR OTHER GUESTS

guest_index = guest_list[1]
message_invitation = "\nDear " + guest_index.title() + " I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)


guest_index = guest_list[2]
message_invitation = "\nDear " + guest_index.title() + " I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)


guest_index = guest_list[3]
message_invitation = "\nDear " + guest_index.title() + " I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

