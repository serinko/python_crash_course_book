# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

# user will decide when to quit, using the while loop
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter '' to end the program. "
message = ""
active = True

while active:
    message == input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
