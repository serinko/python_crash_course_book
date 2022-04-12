import csv

filename = 'data/the_csv_file_format/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # This passes the next line (1st = header)
    # print(header_row)
    # # Outcome is comma-separated line

    for index, column_header in enumerate(header_row):
        print(index, column_header)