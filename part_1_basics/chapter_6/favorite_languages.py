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
print(f"Sarah's favorite language is {language}")
# It is easier and nicer to rrad to print with a variable.
# For the first time we can see that we use {} in print instead of +
