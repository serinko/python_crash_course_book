cities = {
    'amed': {
        'country': 'kurdistan',
        'population': 1783431,
        'interesting_fact': 'Amed is the biggest city in northern Kurdistan'
                            'region called Bakur. Amed has been a foundation '
                            'for peoples struggle for freedom. Main liberatory '
                            'events in recent history are:'
                            '\n\tEarly 1980s prison uprising'
                            '\n\tUprising in the district Sur (in the old town),'
                            'followed by heroic resistance (2015,2016). ',
    },
    'tabor': {
        'country': 'bohemia',
        'population': 34119,
        'interesting_fact': 'Tábor was founded in the spring of '
                            '1420 by Hussites. After the Taborites were '
                            'victorious in the Battle of Tábor. '
                            'The village became the base from which the '
                            'Hussites led their victorious expeditions.',
    },
    'jonestown': {
        'country': 'guyana',
        'population': 918,
        'interesting_fact': "In total, 918 individuals died in Jonestown, "
                            "all but two from apparent cyanide poisoning "
                            "(a significant number of whom were injected "
                            "against their will), in an event termed "
                            "'revolutionary suicide'. The poisonings in "
                            "Jonestown followed the murder of five others by "
                            "Temple members at Port Kaituma, including "
                            "United States Congressman Leo Ryan, an act that "
                            "Jones ordered. Four other Temple members "
                            "committed murder–suicide in Georgetown at Jones'"
                            " command.",
    },
}

print(f"Here are {str(len(cities))} cities, and some info about them: ")
for city, information in cities.items():
    print(f"\nCity: {city.title()}")
    country = information['country']
    population = information['population']
    fact = information['interesting_fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {str(population)}")
    print(f"\tInteresting fact: {fact}")
