"""Module of a ship behaviour and modelation for alien_1"""
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
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        # If we kept the rect as the object - it would only be able to store
        # an integer. Variable (x) can store decimals
        self.y = float(self.rect.y)

        # Movement flags
        # defined in the main program. If no key is pressed, the ship is stable
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update's the ship's position based on the movement flags."""
        # Update the ships value, not the rect
        # Make sure the ship stays within the screen
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # Move ship to the right
            self.y += self.settings.ship_speed

        if self.moving_up and self.rect.moving_up > 0:
            self.y -= self.settings.ship_speed

        # update rect object from self.x.
        # That actually controls the position of the ship
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
