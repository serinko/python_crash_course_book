# Notes: Data visualisation in Python
import matplotlib.pyplot as plt

# Dependencies
- Python
- Matplotlib 

`$ python -m pip install --user matplotlib` or 

`$ python3 -m pip install --user matplotlib`

# Ploting graphs

| **syntax**					 	                | **action**							                     |
|----------------------------------|---------------------------------------|
| import matplotlib.pyplot			      | contains functions for charts & plots |
| subplots()					                  | generate plot(s) in one figure        |
| fig (*variable*)                 | entire figure/ collection of plots    |
| ax (*variable*)                  | single plot in a figure               |
| plot()                           | plot the data                         |
| plt.show() (*pyplot as plt*)     | display plot in Matplotlib's viewer   |
| ax.plot(plot, linewidth) | control the thickness of plotted line |
| ax.set_title("title", fontsize)  | set caption of the plot               |
| ax.set_xlabel("title", fontsize) | set caption of x axel                 |
| ax.set_ylabel("title", fontsize) | set caption of y axel                 |
| ax.tick_params(axis='both', labelsize) | style 'both' tick marks         |



