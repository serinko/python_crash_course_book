pet_0 = {
    'owners_firstname': 'rick',
    'owners_last_name': 'cowboy',
    'pet': 'ponny',
    'pet_name': 'hurricane',
    'pet_age': 5
}

pet_1 = {
    'owners_firstname': 'mathew',
    'owners_last_name': 'tough',
    'pet': 'dog - chiwawa',
    'pet_name': 'killer',
    'pet_age': 16
}
pet_2 = {
    'owners_firstname': 'lena',
    'owners_last_name': 'muller',
    'pet': 'pig',
    'pet_name': 'cozy',
    'pet_age': 1
}

pets = []
pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

print("List of people and their pets:")

for pet in pets:
    # for key,value in person.items():
    owner_name = (f"{pet['owners_firstname']} {pet['owners_last_name']}")
    animal = (f"{pet['pet']}")
    pet_name = (f"{pet['pet_name']}")
    pets_age = (f"{pet['pet_age']}")

    print(f"\nOwner's name: {owner_name.title()}")
    print(f"Animal/pet: {animal}")
    print(f"Name of pet: {pet_name.title()}")
    if pets_age > str(1):
        print(f"Age of pet: {str(pets_age)} years")
    else:
        print(f"Age of pet: {str(pets_age)} year")
