import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as the program is active.
while True:
    # make a random walk
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values, rw.y_values,
        c=point_numbers, cmap=plt.cm.Greens,
        edgecolors='none', s=30
    )
    # Emphasize the first and the last points
    ax.scatter(
        0, 0, c='blue',
        edgecolors='none',
        s=100
    )
    ax.scatter(
        rw.x_values[-1],
        rw.y_values[-1],
        c='red',
        edgecolor='none',
        s=100
    )

    plt.show()

    prompt = 'Make another walk? (y/n): '
    keep_running = input(prompt)
    if keep_running == 'n':
        break
