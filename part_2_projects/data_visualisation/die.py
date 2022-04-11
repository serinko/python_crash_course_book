from random import randrange


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six sided die."""

        self.num_sides = num_sides

    def roll(self):
        """Return a rendom value between 1 and number of sides."""
        return randrange(1, self.num_sides + 1)
#
#     def print(self):
#         for i in range(10):
#             i = self.roll()
#             print(i)
#
#
# die = Die()
# die.print()
