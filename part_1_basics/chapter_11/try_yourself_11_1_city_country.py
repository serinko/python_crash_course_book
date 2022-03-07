"""Returns a single string of formatted city, country"""


def get_cities_formatted(city, country, population=None):
    if population:
        cities_formatted = \
            f"{city}, {country} - population {population}"
    else:
        cities_formatted = f"{city}, {country}"
    return cities_formatted.title()
