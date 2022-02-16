# Lets use examples from before, make sure that:
# The code wil work even if:
# an empty dictionary is used or,
# an empty list nested in a dictionary is used

# lists shall be printed inm the same line, nicely formatted.

# We use the favorite languages program from this chapter
favorite_languages_programming = {
    'jen': ['python'],
    'sarah': ['c'],
    'edward': ['ruby'],
    'phil': ['python'],
}

# add few more to make lists nested in dictionaries
favorite_languages_programming['jen'] = ['python', 'ruby']
favorite_languages_programming['edward'] = ['ruby', 'go']
favorite_languages_programming['phil'] = ['python', 'haskell']

# Adding a user with no favorite language
favorite_languages_programming['vojak'] = []

# control print
# print(favorite_languages_programming)

# Adding an empty dictionary
favorite_languages_speaking = {}

print(f"Thank you for taking the poll."
      f"\nHere is the list of people and their favorite "
      f"programming languages:\n")

if favorite_languages_programming:
    for person, languages in favorite_languages_programming.items():
        if len(languages) == 0:
            print(f"\t{person.title()}, did not submit any favorite "
                  f"programming language to the poll.")
        elif len(languages) == 1:
            print(
                f"\t{person.title()}'s favorite language is {languages[0].title()}")
        elif len(languages) > 1:
            languages_formatted = ", ".join(languages)
            message = (f"{person.title()}'s "
                       f"favorite programming languages are:")
            print(f"\t{message} {languages_formatted.title()}.")
else:
    print(
        "No one submitted to the poll of favorite speaking languages."
    )

print(
    f"\n\nHere is the list of people and their favorite speaking languages:\n")

if favorite_languages_speaking:
    for person, languages in favorite_languages_speaking.items():
        if len(languages) == 0:
            print(f"\t{person.title()}, did not submit any favorite speaking "
                  f"language to the poll.")
        elif len(languages) == 1:
            print(
                f"\t{person.title()}'s favorite language is {languages[0].title()}")
        elif len(languages) > 1:
            languages_formatted = ", ".join(languages)
            message = (f"{person.title()}'s "
                       f"favorite speaking languages are:")
            print(f"\t{message} {languages_formatted.title()}.")
else:
    print(
        "No one submitted to the poll of favorite speaking languages."
    )
