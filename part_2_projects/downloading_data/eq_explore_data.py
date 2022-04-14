import json

# Explore the structure of the data
filename = 'data/mapping_global_data_sets/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/mapping_global_data_sets/data/eq_data_1_day_m1.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
# formatting the data with a proper data structure

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# Pulling the magnitudes
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
