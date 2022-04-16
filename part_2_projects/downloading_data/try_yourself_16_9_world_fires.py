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
        time_index = header_row.index('acq_time')

        try:
            bright = float(row[bright_idx])
            lon = float(row[lon_index])
            lat = float(row[lat_index])
            date_time = f"{row[date_index]}, {row[time_index]}"
            hover_date_time = \
                datetime.strptime(date_time, '%Y-%m-%d, %H%M')

        except IndexError:
            print(f"Missing data")
        else:
            brigthnes.append(bright)
            lons.append(lon)
            lats.append(lat)
            hover_dates.append(hover_date_time)

# Map the earthquakes
# data = [Scattergeo(lon=lons, lat=lats)]
# alternative:
data = [{
    'type': 'scattergeo',
    'lon': lons[:500],
    'lat': lats[:500],
    'text': hover_dates[:500],
    'marker': {
        'size': 20,
        'color': brigthnes,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Brightnes'}
    }
}]

my_layout = Layout(title='World Fires 7 Days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
