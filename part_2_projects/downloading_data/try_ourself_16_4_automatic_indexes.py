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

    # Get dates and high and low temperatures from this file.
    s_dates, s_highs, s_lows = [], [], []
    for row in reader:
        idx_date = header_row.index('DATE')
        idx_high = header_row.index('TMAX')
        idx_low = header_row.index('TMIN')
        current_date = datetime.strptime(row[idx_date], '%Y-%m-%d')
        high = int(row[idx_high])
        low = int(row[idx_low])
        s_dates.append(current_date)
        s_highs.append(high)
        s_lows.append(low)

filename = 'data/the_csv_file_format/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dv_dates, dv_highs, dv_lows = [], [], []
    for row in reader:
        idx_date = header_row.index('DATE')
        idx_high = header_row.index('TMAX')
        idx_low = header_row.index('TMIN')
        current_date = datetime.strptime(row[idx_date], '%Y-%m-%d')
        try:
            high = int(row[idx_high])
            low = int(row[idx_low])
        except ValueError:
            print(f"Missing data for D.V. {current_date}")
            dv_dates.append(current_date)
            dv_highs.append(dv_highs[-1])
            dv_lows.append(dv_lows[-1])

        else:
            dv_dates.append(current_date)
            dv_highs.append(high)
            dv_lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(s_dates, s_highs, c="#FF8095", alpha=0.8)
ax.plot(s_dates, s_lows, c="#CC99FF", alpha=0.8)
ax.fill_between(s_dates, s_highs, s_lows, facecolor="#B3BFFF", alpha=0.2)

ax.plot(dv_dates, dv_highs, c="#FF9999", alpha=0.8)
ax.plot(dv_dates, dv_lows, c="#99AAFF", alpha=0.8)
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor="#B3BFFF",
                alpha=0.2)

# Format plot.
ax.set_title(
    "Daily high and low temperatures in Sitka and Death Valley - 2018",
    fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
# draws the date labels diagonally to prevent them from overlapping
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
