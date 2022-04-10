from random import choice


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of walk."""
        self.num_points = num_points

        # All walk starts at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):

        # Decide which direction to go and how far to go in that direction.
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance
        return [x_step, y_step]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps util the walk reaches the designed length
        while len(self.x_values) < self.num_points:

            [x_step, y_step] = self.get_step()
            # y_step = self.get_step()[1]
            # destructuring way

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            # [-1] = indexing the last value in the list

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(x)
            self.y_values.append(y)
