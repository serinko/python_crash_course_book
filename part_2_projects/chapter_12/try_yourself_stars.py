import sys

import pygame


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

    def settings:
        screen_width = 1920
        screen_height = 1060

        bg_color = (0, 17, 26,)
        # Ship settings
        # Setting the speed like this will make much easier to change it later

    def star


    def _create_sky(self):
        """Create the fleet of aliens"""

        # Create an alien and find a number of aliens fitting a row
        # Spacing between each = width of one alien
        # Make an alien
        alien = Alien(self)
        # self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        # counts # fitting aliens per row
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # // sgn is a floor division, drops off all the reminder.
        # Always returns an integer

        # Determine the number of aliens
        ship_height = self.ship.rect.height
        available_space_y = \
            (self.settings.screen_height - (3 * alien_height) - ship_height)

        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            # Create the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

                # Two nested loops when one make a row from an alien
                # Another makes a plot of rows from one row

    def _create_star(self, star_number, row_number):
        """Create alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        # Adds to the group aliens in Sprite (in __init__)


    def _check_events(self):
        # _method() is known as a helper method
        """Respond to key-presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)