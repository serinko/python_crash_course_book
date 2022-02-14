favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_of_people = ['edward', 'erin', 'mariana', 'isac', 'anna', ]

for name in favorite_languages.keys():

    if name in poll_of_people:
        print(f"\nHey {name.title()}, "
              f"we would like to invite you to our poll "
              f"of favorite languages.")
    else:
        language = favorite_languages[name]
        print(
            f"\nHey {name.title()}, thank you for joining the poll. "
            f"We are happy to see that you like to use {language.title()}."
        )
