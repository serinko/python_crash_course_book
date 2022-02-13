alergies_diets = {
    'ben': ['soya', 'gluten', 'cucumber'],
    'lena': ['gluten', 'vegetarian diet'],
    'percival': ['vegan diet', 'nuts'],
    'clara': ['keto diet', 'no carbs', 'no starch', 'alergy beans', ],
}

for name, diet in alergies_diets.items():
    print(f"{name.title()}'s diet, alergies and food info:")
    for food in diet:
        print(f"\t- {food}")
    print("\n")
