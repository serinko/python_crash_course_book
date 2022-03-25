import sys

import pygame


class Star:
    def __init__(self, StarSky):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = StarSky.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new line near to the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien exact horizontal position
        self.x = float(self.rect.x)

class StarSky:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        # Run he game in full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Star Sky")

        self.stars = pygame.sprite.Group()

        self._create_sky()

        # Set the background color
        self.bg_color = (0, 17, 26)

    def run:
        self._update_screen()

    def settings:
        screen_width = 1920
        screen_height = 1060

        bg_color = (0, 17, 26,)
        # Ship settings
        # Setting the speed like this will make much easier to change it later



    def _create_sky(self):
        """Create the fleet of stars"""

        star = Star(self)
        # self.aliens.add(alien)
        star_width, star_height = star.rect.size
        # counts # fitting aliens per row
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_star_x = available_space_x // (2 * star_width)
        # // sgn is a floor division, drops off all the reminder.
        # Always returns an integer

        # Determine the number of aliens

        available_space_y = \
            (self.settings.screen_height - (3 * star_height))

        number_rows = available_space_y // (2 * star_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            # Create the first row of aliens
            for star_number in range(number_star_x):
                self._create_star(star_number, row_number)

                # Two nested loops when one make a row from an alien
                # Another makes a plot of rows from one row

    def _create_star(self, star_number, row_number):
        """Create alien and place it in the row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star.rect.height * row_number
        self.star.add(star)
        # Adds to the group aliens in Sprite (in __init__)


    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    sky = StarSky()
    sky.run()
