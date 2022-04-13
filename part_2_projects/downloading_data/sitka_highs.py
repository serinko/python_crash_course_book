import csv

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

    # Get High temperatures from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    # The loop started on line 2 as we moved before to the next() once

print(highs)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
