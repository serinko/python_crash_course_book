def make_car(manufacturer, model, **car_info):
    """Builds a dictionary with information about a car,
    manufacturer and model are required, the rest of info can be defined"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car_1 = make_car('subaru', 'evolution', color='blue', offroad=True)
car_2 = make_car('skoda', 'fabia', color='black', combi=True)

print(car_1)
print(car_2)
