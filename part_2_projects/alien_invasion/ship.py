import pygame
from random import choice
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        ships = []
        ship_1 = ships.append('images/spaceship_1.bmp')
        ship_2 = ships.append('images/spaceship_2.bmp')
        ship = choice(ships)
        self.image = pygame.image.load(ship)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        # If we kept the rect as the object - it would only be able to store
        # an integer. Variable (x) can store decimals
        self.x = float(self.rect.x)

        # Movement flags
        # defined in the main program. If no key is pressed, the ship is stable
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update's the ship's position based on the movement flags."""
        # Update the ships value, not the rect
        # Make sure the ship stays within the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move ship to the right
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x.
        # That actually controls the position of the ship
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


class ShipSB(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        ship = 'images/spaceship_1.bmp'
        self.image = pygame.image.load(ship)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.75)
        # rotozoom = rotate angle, zoom by * multiplication
        # rotozoom(src, angle, zoom)
        self.rect = self.image.get_rect()
