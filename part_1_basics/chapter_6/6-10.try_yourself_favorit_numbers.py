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
            f"\nThis is {character.title()}'s favorite number: "
            f"{numbers[0]}")
    else:
        print(f"\nThese are the {character.title()} favorite numbers:")
        print(*numbers, sep=', ')
        #
        # for number in numbers:
        #     print(f"\t{number}")
