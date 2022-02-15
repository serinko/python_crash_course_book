# Dictionary with similar objects
# object = {many informations} or
# one_kind_of_information = {many objects}
# This is a dictionary of similar objects, one information

favorite_languages = {
    'jen': 'python',
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

print("\n")

# VALUES - looping thorugh all values using values() function
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    # this method does not check for repeats
    print(language.title())

print("\n")

# set() function makes sure to return every value in unique fashion
for language in set(favorite_languages.values()):
    print(language.title())
print("\n")

# set can be build with {} braces.
# can be easily mistaken with a list. Sets have no key-value pairs!
# ~ set = {'value_0', 'value_1', 'value_2'}
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
print("\n")

# Adding new languages to these people by modifying the value
# changing it into a list
favorite_languages['jen'] = ['python', 'ruby']
favorite_languages['edward'] = ['ruby', 'go']
favorite_languages['phil'] = ['python', 'haskell']

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
print("\n")
# Do NOT nest deeper than this level - if you must nest deeper
# Slow down and think about SIMPLER SOLUTION!

# We can use if and len() function to pritn different message for:
# ppl with one or with  multiple languages.
# Only multiple will be printed as a for loop list:
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {language.title()}.")
    else:
        print(f"\n{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
