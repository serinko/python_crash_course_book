import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values,
           cmap=plt.cm.Greens, s=10)

# set chart title and label axes
ax.set_title("Cubes", c='green', fontsize=35)
ax.set_xlabel("X value", c='green', fontsize=24)
ax.set_ylabel("X^3", c='green', fontsize=24)

# set size of thick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
ax.axis([0, 5001, 0, 125000000001])

plt.show()
