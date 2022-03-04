message = \
    "Welcome to the 'Programming poll'. \n " \
    "We would like to ask programers to enter their reasons," \
    " why are they programming."

prompt = "\n\nPlease enter a reason:  "
prompt += ("(enter 'q' when finished)")
file = 'programming_poll.txt'

with open(file, 'a') as p_poll:
    name = input("\nWhat is your username: ")
    p_poll.write(f"user: {name}. Reasons for programming:  ")

    while True:
        reason = input(prompt)
        if reason.lower() != 'q':
            p_poll.write(f"\n\t- {reason}")
        else:
            quit()
            