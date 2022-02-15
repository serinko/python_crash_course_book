person_0 = {
    'first_name': 'joan',
    'last_name': 'from arc',
    'age': 19,
    'city': 'arc',
}

person_1 = {
    'first_name': 'alexander',
    'last_name': 'berkman',
    'age': 65,
    'city': 'vilnia',
}

person_2 = {
    'first_name': 'lucy',
    'last_name': 'parsons',
    'age': 91,
    'city': 'Lucia Carter',
}

people = []
people.append(person_0)
people.append(person_1)
people.append(person_2)

print("THEIR MEMORY LIVES IN OUR STRUGGLE:\n")

for person in people:
    # for key,value in person.items():
    full_name = (f"{person['first_name']} {person['last_name']}")
    city = (f"{person['city']}")
    age = (f"{person['age']}")

    print(f"\nFull name: {full_name.title()}")
    print(f"City of origin: {city.title()}")
    print(f"Age when died: {str(age)}")
