# Dictionary with similar objects
# object = {many informations} or
# one_kind_of_information = {many objects}
# This is a dictionary of similar objects, one information

favorite_languages = {
    'jen': 'pythonn',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
# new variable = dictionary[key], this pulls the value and styles with title()
print(f"Sarah's favorite language is {language}.")
# It is easier and nicer to re  ad to print with a variable.
# For the first time we can see that we use {} in print instead of +

print("\n")

# one can print a sentence using the key-value pair
# items() function can be used for this for loop
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

# Looping through keys in dictionary
# Using keys() method
for name in favorite_languages.keys():
    print(name.title())
    # prints keys only, no value
print("\n")
# this is a defaulf behaviour as if it was just
# ~ for name in favorite_languages:
# so that is an easier one, though the key() method may be easier to read

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    # prints a message to every name (key)

    if name in friends:
        language = favorite_languages[name].title()
        # making a variable for the value in the dictionary
        print(f"\t{name.title()}, I see you love {language}!")
        # Prints a message if name is in friends using language

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n")

# sorted() function to return names in alphabetical order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
