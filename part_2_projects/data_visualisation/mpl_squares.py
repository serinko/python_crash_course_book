import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=24)

# set size of thick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
