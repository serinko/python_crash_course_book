favorite_numbers = {
    'wanderer': 0,
    'magician': 1,
    'seer': 2,
    'temperance': 24,
    'death': 13,

}

for archetype in favorite_numbers:
    print(f"{archetype.title()}: {str(favorite_numbers[archetype])}")
