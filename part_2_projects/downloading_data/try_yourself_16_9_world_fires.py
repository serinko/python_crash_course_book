import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

import matplotlib.pyplot as plt

filename = 'data/mapping_global_data_sets/data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #

    brigthnes, lons, lats, hover_dates = [], [], [], []
    for row in reader:
        bright_idx = header_row.index('bright_ti4')
        lon_index = header_row.index('longitude')
        lat_index = header_row.index('latitude')
        date_index = header_row.index('acq_date')
        try:
            bright = float(row[bright_idx])
            lon = float(row[lon_index])
            lat = float(row[lat_index])
            hover_date = row[5]
        except ValueError:
            print(f"Missing data")
        else:
            brigthnes.append(bright)
            lons.append(lon)
            lats.append(lat)
            hover_dates.append(hover_date)

# Map the earthquakes
# data = [Scattergeo(lon=lons, lat=lats)]
# alternative:
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_dates,
    'marker': {
        'size': [5 * bright for bright in brigthnes],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'}
    }
}]

my_layout = Layout(title='World Fires 7 Days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
