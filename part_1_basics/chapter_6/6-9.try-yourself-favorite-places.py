favorite_places = {
    'irkutsk': 'peter kropotkin',
    'new york': 'emma goldman',
    'sumava': 'karel klosterman'
}

print("People's favorite plases:\n")
for place, name in favorite_places.items():
    print(f"\t{name.title()}: {place.title()}")
