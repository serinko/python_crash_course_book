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
            f"This is {character.title()}'s favorite number: "
            f"{numbers[0]}")
        print("\n")
    else:
        # print(f"\nThese are the {character.title()} favorite numbers:")
        # print(*numbers, sep=', ')

        message = f"\nThese are the {character.title()}'s favorite numbers: "
        print(message, end='')

        for number in numbers:
            print(number, end=', ')
        print("\n")
# end or sep are parameters keeping the items in the same line
# either SEParating them or ENDing them with the given parameter
