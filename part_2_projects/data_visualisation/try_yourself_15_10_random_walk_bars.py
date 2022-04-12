import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline

from random_walk import RandomWalk

# Random walk instance
while True:
    rw = RandomWalk()
    rw.fill_walk()
    
# Make some rolls and store results in a list.
# results = []
# for roll_num in range(50_000):
#     result = die_1.roll() + die_2.roll() + die_3.roll()
#     results.append(result)

roll_num = range(50000)
results = [
    (die_1.roll() + die_2.roll() + die_3.roll())
    for i in roll_num
]

# Analyze the results.
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
# for value in range(3, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [
    results.count(value) \
    for value in range(3, max_result + 1)
]

# print(frequencies)
#
# print(results)
# print(len(results))

# Visualise the results
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequecy of Result'}
my_layout = Layout(
    title='Results of rolling three D6 50000 times',
    xaxis=x_axis_config,
    yaxis=y_axis_config
)
offline.plot(
    {
        'data': data,
        'layout': my_layout,
    },
    filename='d6_d6_d6.html'
)
