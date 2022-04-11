# Notes: Data visualisation in Python
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Dependencies
- Python
- Matplotlib 

`$ python -m pip install --user matplotlib` or 

`$ python3 -m pip install --user matplotlib`

# Ploting Graphs & Plots

## Simple Graphs

| **syntax**					 	             | **action** |
|-------------------------------|-----------|
| import matplotlib.pyplot			   | contains functions for charts & plots |
| fig, ag = plt.subplots()       | generate plot(s) in one figure |
| fig (*variable*)              | entire figure/ collection of plots |
| ax (*variable*)               | single plot in a figure |
| plot(x_value, y_value)        | plot the data |
| plt.show() (*pyplot as plt*)  | display plot in Matplotlib's viewer |
| ax.plot(plot, linewidth)      | control the thickness of plotted line |
| ax.set_title("title", fontsize) | set caption of the plot |
| ax.set_xlabel("title", fontsize) | set caption of x axel |
| ax.set_ylabel("title", fontsize) | set caption of y axel |
| ax.tick_params(axis='both', labelsize) | style 'both' tick marks |
| plt.savefig('squares_plot.png',bbox_inches='tight') | save plot, trims white space |
| feg, ax = plt.subplots(figsize=*(15,9)*,dpi=*?*) | tuple parameter to fit the screen |

## Built-in Styles
ax.plot(*plot, linewidth*) is a clasic plot with a line, scatter() is way to create plots, using dots.

| **syntax**					 	      | **action**	 |
| ------------------------ | ------------- |
| ax.scatter(*x,y*) | plot a single plot with given values |
| ax.scatter(*x,y, s=20*) | size of the dots used draw the graph | 
| ax.tick_params(*axis='both', ehich='major', labelsize=*) | style 'both' tick marks      |

Run Python and check for styles:
```
>>> import matplotlib.pyplot as plt
>>> plt.style.available
['seaborn-dark', 'seaborn-darkgrid'
--snip--
```
Check them out and choose the one you like:

| **syntax**					 	          | **action**	          |
|----------------------------|----------------------|
| plt.style.use(*'style'*) | generate plot in the given 'style' |
| ax.axis([*xrange, yrange*]) | specify the rage of each axis (4 values) |

**List of build-In Styles:**
- Solarize_Light2
- _classic_test_patch
- _mpl-gallery
- _mpl-gallery-nogrid
- bmh
- classic
- dark_background
- fast
- fivethirtyeight
- ggplot
- grayscale
- seaborn
- seaborn-bright
- seaborn-colorblind
- seaborn-dark
- seaborn-dark-palette
- seaborn-darkgrid
- seaborn-deep
- seaborn-muted
- seaborn-notebook
- seaborn-paper
- seaborn-pastel
- seaborn-poster
- seaborn-talk
- seaborn-ticks
- seaborn-white
- seaborn-whitegrid
- tableau-colorblind10

## Calculating Data Automatically

Writing lists by hand may be inefficient in time and risk to human error. 

**Squares** of x_values = [1,2,3,4,5,6,7,8,9,10] instead of being written manually as y_values = [1,4,9..] can be calculated in Python. Then the code look like this:

```python
x_values = range(1,11) # mind the range ends one before its cap
y_values = [x**2 for x in x_values] # a list comprehension generates the y_values by looping through the x_values
```
## Defining Custom Colors
- To change the color pass 'c' to scatter() with the name of the color or RGB.

| **syntax**					 	 | **action**	         |
|---------------|---------------------|
| ax.scatter(*x_values, y_values, c='color',s=10*) | change the color of graph |
| *c='red';c=(0,0.8,0)* | name or RGB for color |

### Using a Colormap
- A series of colors - gradient that moves from a starting point to an ending color.
- Emphasizes a patter in the visualisation

| **syntax**					 	 | **action**	 |
|---------------|--|
| ax.scatter(*x_values, y_values, c=y_values,cmap=plt.cm.Blues,s=10*) | pass list Y_values and asign a colormap |
| ...(..edgecolors='none', s=...) | take off the edge color from the dots |
- Pyplot available colormaps are at *https://matplotlib.org/*; go to ***Examples***, down to ***Color*** and ***Colormap reference***.

## Saving Plots automatically

- plt.show() runs our visualisation
- plt.savefig('file_name.png',bbox_inches='tight')
  - save plot into the given file_name
  - bbox_inches='tight' - trims white space; this argument can be omitted.

# Random Walks

A random walk is a path that as no clear direction - is determined by a series of random decisions, each of which is left entirely to chance.
Random walks have practical applications in nature, physics, bilogy, chemistry and economics.

## Creating Random Walk Class

- **Needs three attributes:**
  - A variable to store the number of points in the walk
  - Two lists to store x- and y- coordinate values of each point in the walk

- **Two methods:**
  - __init__() method
  - fill_walk() - calculate the points

- **choice()** method is called from the random module:
```python
from random import choice
```
See an example in *random_walk.py*.

## Plotting the Random Walk

A simple example of using pyplot for the instance of RandomWalk

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk
rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
```
### Emphasize the Starting and Ending Points

- After the main plot line of code (ax. scatter()) add:

```python
# Emphasize the starting point - blue and larger size
ax.scatter(
    0, 0, c='blue',
    edgecolors='none',
    s=100
)
# Emphasize the ending point - red and larger size
ax.scatter(
    rw.x_values[-1],
    rw.y_values[-1],
    c='red',
    edgecolor='none',
    s=100
)
```

## Remove the Axes
To remove x and y axes, run:
```python
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
```

# Plotly

[*https://plot.ly/python*](https://plot.ly/python)

`$ python -m pip install --user plotly` or


`$ python3 -m pip install --user plotly`

# Making a Histogram

```python
from plotly.graph_objs import Bar, Layout
from plotly import offline
```
**Visualisation of die.py in die_visual.py**
```python
x_values = list(range(1, die.num_sides + 1))
# Plotly does not accept range - create a list
data = [Bar(x=x_values, y=frequencies)]
# Plotly class Bar represent data set - formatted as a bar chart
# need list of x-values and y-values
# Wrapped in [] bcs data set can have multiple elements

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequecy of Result'}
my_layout = Layout(
    title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config,
    yaxis=y_axis_config
)
# Configuration of axis stored as dictionay
# data and lay out objects
# accepts name of the file where to store the graph


offline.plot(
    {
        'data': data,
        'layout': my_layout,
    },
    filename='d6.html'
)
```