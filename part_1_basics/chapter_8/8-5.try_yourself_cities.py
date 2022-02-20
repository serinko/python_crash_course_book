def describe_city(name_city, country_city='island'):
    """Displays name and a country of a city"""
    print(f"{name_city.title()} is in {country_city.title()}.")


describe_city('reykjavik')
describe_city('moscow', 'russia')
describe_city(name_city='khairo', country_city='egypt')