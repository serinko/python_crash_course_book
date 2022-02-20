def city_country(city, country):
    """Dictionary of a formatted city and country"""
    formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()


print(f"{city_country('santiago', 'chile')}")
print(f"{city_country('ramalan', 'palestine')}")
print(f"{city_country('bilbao', 'basq country')}")
