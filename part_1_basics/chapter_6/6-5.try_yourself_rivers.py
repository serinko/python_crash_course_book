rivers = {
    'nile': 'egypt',
    'donau': 'slovakia',
    'amazon': 'bolivia',
}

for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}.")
print("\n")

print("This is a list of the rivers in the dictionary.:")
for river in sorted(rivers.keys()):
    print(river.title())
print("\n")

print("Here are all the countries we mention in the dictionary.:")
for country in rivers.values():
    print(country.title())
