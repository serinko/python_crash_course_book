import csv

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
