from random import choice as ch


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of walk."""
        self.num_points = num_points

        # All walk starts at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

        