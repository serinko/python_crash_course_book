import sys
import pygame
from pygame.sprite import Sprite


class RainDrop(Sprite):
    def __init__(self, StarSky):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = StarSky.screen
        self.settings = Settings()

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/raindrop.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        """Move the alien to the right and left"""
        self.y += (self.settings.raindrop_speed * \
                   self.settings.rain_direction)

        self.rect.y = self.y

    def _check_edges(self):
        """Return True if alien is at the dge of the screen"""
        screen_rect = self.screen.get_rect()

        if self.rect.top >= screen_rect.bottom:
            return True


class Settings():
    def __init__(self):
        # self.screen_width = 1920
        # self.screen_height = 1060
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.bg_color = (0, 17, 26,)

        # Raindrop settings
        self.raindrop_speed = 1.0
        self.rain_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left
        self.rain_direction = 1


class Rain:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star Sky")
        self.raindrops = pygame.sprite.Group()
        self._create_rain()
        self.bg_color = (0, 17, 26)

    def _check_events(self):
        """Respond to key-presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def run(self):
        while True:
            self._check_events()
            self._update_sky()
            self._update_screen()

    def _update_sky(self):
        """
        Check if the fleet is at an edge,
        then update position of all aliens in the fleet."""
        self._check_edges()
        self.raindrops.update()

    def _create_rain(self):
        """Create the fleet of stars"""
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width
        number_raindrop_x = available_space_x // raindrop_width
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // raindrop_height

        # Create the full fleet of stars
        for row_number in range(number_rows):
            # Create the first row of stars
            for raindrop_number in range(number_raindrop_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create alien and place it in the row"""
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = 1.18 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = 1.18 * raindrop.rect.height * row_number
        self.raindrops.add(raindrop)
        # Adds to the group aliens in Sprite (in __init__)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    sky = Rain()
    sky.run()
