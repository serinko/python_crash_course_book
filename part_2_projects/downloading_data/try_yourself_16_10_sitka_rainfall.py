import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/the_csv_file_format/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # This passes the next line (1st = header)

    # print(header_row)
    # # Outcome is comma-separated line

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # # Outcome is list of index and value of items in the header

    # Get dates and the rainfall
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = int(row[3])
        dates.append(current_date)
        rainfall.append(rain)
    # The loop started on line 2 as we moved before to the next() once

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rain, c='purple', alpha=0.8)
# ax.plot(dates, lows, c='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily rainfall - 2018, Sitka", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
# draws the date labels diagonally to prevent them from overlapping
ax.set_ylabel("Rainfall", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
