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
        edgecolors='none', s=15
    )
    plt.show()

    prompt = 'Make another walk? (y/n): '
    keep_running = input(prompt)
    if keep_running == 'n':
        break
