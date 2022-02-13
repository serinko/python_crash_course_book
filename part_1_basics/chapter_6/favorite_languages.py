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
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
