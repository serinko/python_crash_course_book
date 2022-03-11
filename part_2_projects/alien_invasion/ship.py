import pygame
from random import choice


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
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
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update's the ship's position based on the movement flags."""
        # Update the ships value, not the rect
        if self.moving_right:
            # Move ship to the right
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

        # update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
