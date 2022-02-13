person = {
    'first_name': 'joan',
    'last_name': 'from arc',
    'age': 19,
    'city': 'arc',
}

# Print every information
print("First name: " + person['first_name'])
print("Second name: " + person['last_name'])
# Same thing, but new formating style:
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

print("\n")

# Possible to use a loop to print each information in key: value fashion
for item in person:
    print(item + ": " + str(person[item]).title())
