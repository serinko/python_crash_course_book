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
# It is easier and nicer to rrad to print with a variable.
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
