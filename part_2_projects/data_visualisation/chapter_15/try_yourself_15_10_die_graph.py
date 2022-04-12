import matplotlib.pyplot as plt

from die import Die

# Create D6 and D10
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list.
# results = []
# for roll_num in range(50_000):
#     result = die_1.roll() + die_2.roll() + die_3.roll()
#     results.append(result)

roll_num = range(50_000)
results = [ \
    (die_1.roll() + die_2.roll()) \
    for i in roll_num \
    ]

# Analyze the results.
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(3, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [ \
    results.count(value) \
    for value in range(2, max_result + 1) \
    ]

# print(frequencies)
#
# print(results)
# print(len(results))

# Visualise the results
x_values = list(range(2, max_result + 1))
y_values = frequencies

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, c='purple', linewidth=20)

# set chart title and label axes
ax.set_title("Two D6 - 50k times thrown", c='green', fontsize=35)
ax.set_xlabel("Sumary", c='green', fontsize=24)
ax.set_ylabel("Frequency", c='green', fontsize=24)

# set size of thick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# # set the range for each axis
# ax.axis([2, 12, 0, 50])

plt.show()
