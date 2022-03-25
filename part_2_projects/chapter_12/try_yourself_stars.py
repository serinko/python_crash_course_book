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
