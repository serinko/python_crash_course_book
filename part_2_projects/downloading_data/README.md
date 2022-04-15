# Notes: DOWNLOADING DATA

- Ability to analyze and discover patterns and connections out of sight
- Formats: CSV, JSON

## Dependencies

- Python3+
  - Matplotlib
  - Plotly
  - (ensure csv and json modules work properly)

# The CSV File Format
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

Sometimes the field is empty and this would return a ValueError.
We can use try-except-else block to print the missing value and continue examining the data:

The code:
```python
# --snip--
dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:                
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:  
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# --snip--
```

- Make sure the fields were empty as ValueError can appear when numbers aren't base-10
- then the solution is not an exception but using ***float()***
- Other time *continue* or *remove()* or *del* can be used.

- Find an approach that works and the result is an accurate visualisation.

## Donwloading Your Own (weather) Data

**Steps to download the data (weather):**
- *Check the book on the page 345/346 for a detailed guide*

## Automatic Indexes

- Instead of hard-coded rwo index, we can make a call for an index representing the value and save it in a variable.
- code: `index = mylist.index(element)`
- In the program *try_yourself_16_4_automatic_indexes.py* it looked like this:

```python
# --snip--
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
# --snip--
```

# Mapping Global Data Sets: JSON Format

## Downloading Earthquake Data
Using the excersise json file from the book, the source of earth quake data is:
*[earthquake.usgs.gov/earthquakes/feed/](https://earthquake.usgs.gov/earthquakes/feed/)*

## Examining JSON Data
- If the json file seems too hard too read, use Python to format it
```python
import json

# Explore the structure of the data
filename = 'data/mapping_global_data_sets/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/mapping_global_data_sets/data/eq_data_1_day_m1.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
# formating the data with a proper data structure
```
- **Metadata**: Time and source of the data set
- geoJSON file is location-based
- **key "features"**: stores the main information
- every item in the list corresponds to a single earthquake
- as much info about each eartquake in a dictionary
- nested disctionaries in a list
- **key properties**: a lot of info about each earthquake
- **key mag**: maginitude of each e.q. - values we are the most interested in
- **key geometry**: show where e.q. occurred.
- **key coordinates**: longitude and latitude
  - longitude and latitude (x.Y) convention used in JSON
  
*The file contains much more nesting than we use when writing code, still Python can handle that complexity.*

### List of All EarthQuakes

in the JSON file **'count'**: 158

We can make sure to capture all the features:
```python
# --snip--
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
```
## Extracting Magnitudes
 
- If the value we are looking for is in a nested dictionary, we can use a double key:

```python
# --snip--
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
```
- each in the list we made is stored in the variable mag and stored in the list og mags

## Extracting Data Location

- Location is stored under the key "geometry", inside is "coordinates" key.
- First two values is longitude and latitude

```python
# --snip--
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)    
```

## Building a World Map

```python
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# --snip-- 

# Map the earthquakes
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
```

- Scattergeo: a chart type, Layout: a class
- plotly.offline: offline module to render the map
- define a list called data - inside create a Scattergeo object with the coordinates
  - Scattergeo allow us to overlay a scatter plot with the coordinate lists
- Give it a title
- Create a dictionary called fig to call for the data and the layout (title)
- Pass fig to the plot, with a descriptive name of the output

### A Different Way of Specifying Chart Data
change:
```python
data = [Scattergeo(lon=lons, lat=lats)]
```
to:
```python
data=[{
  'type': 'scattergeo',
  'lon':lons,
  'lat':lats,
  'marker':{
    'size':[5*mag for mag in mags],
  }
}]
```
- Plotly offers a variety of customizations which can be done on data series
- 'marker' key specifies the size of each marker on the map
- marker settings are in a dictionary as more settings can be done

### Customizing Maker Colors
- using plotly colorscale
- 