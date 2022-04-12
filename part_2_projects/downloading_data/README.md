# Notes: DOWNLOADING DATA

- Ability to analyze and discover patterns and connections out of sight
- Formats: CSV, JSON

## Dependencies

- Python3+
  - Matplotlib
  - Plotly
  - (ensure csv and json modules work properly)

## The CSV File Format
*comma-separated values*

resources: *[nostarch.com/pythoncrashcourse2e/](https://nostarch.com/pythoncrashcourse2e/)*

- make a folder called *data* in the same directory of this chapter

### Parsing the CSV File Headers

- Python's csv parses the lines in CSV file
- refference *sitka_highs.py* 

| **syntax** | **action** |
| --- | --- |
| reader = csv.reader(*file.csv*) | pass the file to the object |
| next(reader) | pass the next line (in our case the header) |

### Parsing the CSV File Headers & Their Positions

```python
for index, column_header in enumerate(header_row):
    print(index, column_header)

# returns both index and value of each in the list (loop)
```