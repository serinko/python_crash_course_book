filename = 'guest.txt'
prompt = '\n\nPlease enter your name:  '

with open(filename, 'w') as guest_file:
    name = input(prompt)
    message = f"The guest name is: {name.title()}\n"
    guest_file.write(message)

print("Your name was added. Thank you.")