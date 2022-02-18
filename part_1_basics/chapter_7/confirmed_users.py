# MOVING ITEMS FORM ONE LIST TO ANOTHER
# Start with users that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brendan', 'shane']
confirmed_users = []

# Verify each user until there ar eno more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    # Means the loop is True as long as the list has items in it
    current_user = unconfirmed_users.pop()
    # variable used to pop, append and print each user

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print(f"\nThe following users have been confirmed:")
for user in confirmed_users:
    print(f"\t{user.title()}")

# We can see that the loop prints them backwards
# as the pop() function takes items from the end of the list
