favorite_numbers = {
    'wanderer': [0, 1, 2, 3],
    'magician': [1, 2],
    'seer': [2, 13, 20],
    'temperance': [14, 21],
    'death': [13],

}

for character, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(
            f" This is {character.title()}'s favorite number: {str(numbers)} ")

    else:
        print(f"These are the {character.title()}'s favorite numbers:")
        for number in numbers:
            print(f"\t{number}")
