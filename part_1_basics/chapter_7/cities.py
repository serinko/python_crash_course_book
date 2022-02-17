prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(enter 'Q' when you are finished.) "

while True:
    city = input(prompt)

    if city.lower() == 'q':
        break
    else:
        print(f"I'd love to go to"f' "{city.title()}"!')
        