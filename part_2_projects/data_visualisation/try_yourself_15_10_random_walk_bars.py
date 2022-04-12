import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline

from random_walk import RandomWalk

rw = RandomWalk(50)
rw.fill_walk()

# Visualise the results
x_values = rw.x_values
y_values = rw.y_values
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title': 'Movement Horizontal', }  # 'dtick': 1}
y_axis_config = {'title': 'Movement Vertical'}
my_layout = Layout(
    title='Excercise to make Random walk as bars',
    xaxis=x_axis_config,
    yaxis=y_axis_config
)
offline.plot(
    {
        'data': data,
        'layout': my_layout,
    },
    filename='random_walk.html'
)
