import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn-dark-palette')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=5)

# set chart title and label axes
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Number raised to the 3rd power", fontsize=24)

# set size of thick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
ax.axis([0, 6, 0, 130])

plt.show()
