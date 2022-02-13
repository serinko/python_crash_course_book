alergies_diets = {
    'ben': ['soya', 'gluten', 'cucumber'],
    'lena': ['gluten', 'vegetarian diet'],
}

for name, diet in alergies_diets.items():
    print(f"{name.title()}'s diet, alergies and food info:")
    for food in diet:
        print(f"\t- {food}")
    print("\n")
