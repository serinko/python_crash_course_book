

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
	
print("\n")
	
guest_list.insert(0, 'moses')
guest_list.insert(2, 'andrei')	
	# Added gues moses on index 0 and andrei on index 2
	
guest_list.append('nikola')
	# Added nikola to the end of the list
print(guest_list)
	# To check the current state of the list
	
	# PRINT INVITATION FOR EVERY CURRENT GUEST!
	
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

guest_index = guest_list[4]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

guest_index = guest_list[5]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)


guest_index = guest_list[6]
message_invitation = "\nDear " + guest_index.title() + ", I would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

print("\n")


	# TABLE WILL ARRIVE LATE, ONLY TWO PPL CAN COME
	# Start with 3-6.
	# Print a messagae about table not arriving, only 2 ppl
	# Use pop() to remove one at a time and 
	# use the variable to print message for each of them
	# Print a message to the each of the person on he list (2ppl) that they are invited
	# When done, use del to delete the remaining names and empty the list
	# print the list to make sure it's empty
	
message_table_delayed = "\nDear guests, I have a bad news. Just got informed that the table delivery is delayed and therefore I only have capacity for two guests, I am very sorry for this."
	# Defining variable with the message about delayed table
print(message_table_delayed)
	# Printing that message for the guests
	
	# I will take off the lst added guests.
	# That is 0,2, and then from the end
	
cannot_come = guest_list.pop(0)
	# Defyning that index 0 is no longer invited
	# using pop(function)
message_cannot_come = "\nDear " + cannot_come.title() + ", I am very sorry to inform you, that due to the problems with the delayed table, I must cancell your invitation for today's dinner. I hope to make up for this inconvenience very soon."
	# message is defined including the variable cannt_come
print(message_cannot_come)
	# printing message to the guest's informing that one cannot_come

cannot_come = guest_list.pop(1)
	# Defyning that index 1 cannot come and save t as a variable
	# (2 when 0 was deleted becomes 1)
	# using pop(function)
message_cannot_come = "\nDear " + cannot_come.title() + ", I am very sorry to inform you, that due to the problems with the delayed table, I must cancell your invitation for today's dinner. I hope to make up for this inconvenience very soon."
	# message is defined including the variable cannt_come
print(message_cannot_come)
	# printing message to the guest's informing that one cannot_come

cannot_come = guest_list.pop()
	# Defyning variable when the last guest is deleted/ not invited
	# pop with empty () takes off the last item
	# using pop(function)
message_cannot_come = "\nDear " + cannot_come.title() + ", I am very sorry to inform you, that due to the problems with the delayed table, I must cancell your invitation for today's dinner. I hope to make up for this inconvenience very soon."
	# message is defined including the variable cannt_come
print(message_cannot_come)
	# printing message to the guest's informing that one cannot_come
	
cannot_come = guest_list.pop()
	# Defyning variable when the last guest is deleted/ not invited
	# pop with empty () takes off the last item
	# using pop(function)
message_cannot_come = "\nDear " + cannot_come.title() + ", I am very sorry to inform you, that due to the problems with the delayed table, I must cancell your invitation for today's dinner. I hope to make up for this inconvenience very soon."
	# message is defined including the variable cannt_come
print(message_cannot_come)
	# printing message to the guest's informing that one cannot_come
	
cannot_come = guest_list.pop()
	# Defyning variable when the last guest is deleted/ not invited
	# pop with empty () takes off the last item
	# using pop(function)
message_cannot_come = "\nDear " + cannot_come.title() + ", I am very sorry to inform you, that due to the problems with the delayed table, I must cancell your invitation for today's dinner. I hope to make up for this inconvenience very soon."
	# message is defined including the variable cannt_come
print(message_cannot_come)
	# printing message to the guest's informing that one cannot_come
	
print("\n")	
	
print(guest_list)
	# print for myself to control the state of the list
	
	# Everything is correct, only two guest remained
	# Invite them, by printing an invitation for each of them

guest_index = guest_list[0]
message_invitation = "\nDear " + guest_index.title() + ", despite the changes, I still would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

guest_index = guest_list[1]
message_invitation = "\nDear " + guest_index.title() + ", despite the changes, I still would like to invite you for a dinner at my place, tonight. Hope to see you there."
print(message_invitation)

print("\n")
	
	# Delete everyone fromt he list to clean up

del guest_list[0]	
	# deletes the first indexed guest of the list
del guest_list[0]
	# since only one guest/item was left in the list, its again the 1st [0]

print(guest_list)
	# print myself the list to control that it is empty


	
