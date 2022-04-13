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
### Extracting and reading data

- To get particular data - ie high temperatures in column 5. loop through the file
and asign row[index] to and object you looking for:
```python
highs = []
  for row in reader:
      high = int(row[5])
      highs.append(high)
# int() convert string into numbers
# Then store it in highs
```
- Iw we used next() the loop will start bellow that

## Ploting the Data In a Temperature Chart

Same like in the data_visualisation chapter:
```python
import matplotlib.pyplot as plt

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
```
## The datetime Module
- method `strptime()`
```python
from datetime import datetime
```

| **Argument** | **Meaning** |
| --- | --- |
| %A | Weekday name, such as Monday |
| %B | Month name, such as January |
| %m | Month, as a numner (01 to 12) |
| %d | Day of the month as a number (01-31) |
| %Y | Four digit year, such as 2022 |
| %y | Two difgit year, such as 22 |
| %H | Hour, in 24-hour format (00 to 23) |
| %I | Hour, in 12-hour format (01 to 12) |
| %p | Am or PM |
| %M | Minutes (00 to 59) |
| %S | Seconds (00 to 61) |

**Example:**

```
>>> from datetime import datetime
>>> first_date = datetime.strptime('2018-07-01','%Y-%m-%d')
>>> print(first_date)
2018-07-01 00:00:00
```

### Plotting Dates
*See sitka_highs.py*

- Create two empty lists: dates, highs
- Covert the data information using loop like with the highs and datetime module
- Pass dates and highs (lists) values to `plot()`
- Call `fig.autofmt_xdate()` - draws the date labels diagonally to prevent them from overlapping

## Plotting Lows
We will add to our program low temp's
- Same logic, just adding dates to both plots - highs and lows:

```python
## --snip--
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    # The loop started on line 2 as we moved before to the next() once

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates,lows, c='blue')
## --snip--
```

## Shading an Area in the Chart

Using:

- `fill_between()` method 
- new argument *alpha=* - controls color transparency.
  - 0 = completely transparent, 1 (default) completely opaque


```python
## --snip--
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
## --snip--
```

- aplha=0.5; the lines appear lighter
- *fill_betwwen(x-values, y-values_1, y-values_2, facecolor, aplha)*

## Error Checking

