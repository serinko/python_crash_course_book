def city_country(city, country):
    """Dictionary of a formatted city and country"""
    city_info = {
        'city': city,
        'country': country,
    }
    city
    return city_info


my_city = city_country('santiago', 'chile')
for parameter, argument in my_city.items():
    print(f"{parameter.title()}, {argument.title()}")
