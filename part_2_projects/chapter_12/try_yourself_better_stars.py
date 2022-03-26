import sys
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, StarSky):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = StarSky.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/a_star.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


class StarSky:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star Sky")
        self.stars = pygame.sprite.Group()
        self._create_sky()
        self.bg_color = (0, 17, 26)

    def _check_events(self):
        """Respond to key-presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_sky(self):
        """Create the fleet of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width
        number_stars_x = available_space_x // star_width
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // star_height

        # Create the full fleet of stars
        for row_number in range(number_rows):
            # Create the first row of stars
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)
