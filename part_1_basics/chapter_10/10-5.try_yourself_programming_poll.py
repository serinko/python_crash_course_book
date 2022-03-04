message = \
    "Welcome to Programming poll! \n" \
    "We would like to ask programers to enter their reasons," \
    " why are they programming."

print(message)

prompt = "\n\nPlease enter a reason:  "
prompt += ("\n(enter 'q' when finished)")
file = 'programming_poll.txt'

with open(file, 'a') as p_poll:
    name = input("\nWhat is your username: ")
    p_poll.write(f"\n\nuser: {name}. \nReasons for programming:  ")

    while True:
        reason = input(prompt)
        if reason.lower() != 'q':
            p_poll.write(f"\n\t- {reason}")
            p_poll.flush()
            # pushes an entry from memory to the disk instantly
        else:
            quit()
