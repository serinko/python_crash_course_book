filename = 'guest_book.txt'
prompt = '\n\nHello ad weolcome.'
prompt += 'Please enter your name:  '

with open(filename, 'a') as guests:
    name = input(prompt)
    message = f"- {name.title()}\n"
    guests.write(message)

print("\nYour name was added to a guest book. "
      "Thank you. Have a good visit. ")
