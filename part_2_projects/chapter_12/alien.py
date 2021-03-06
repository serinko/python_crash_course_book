import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    "A Class to represent single alien in the fleet"

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.load("images/alien.bmp")
        self.rect = self.image_get.rect()

        # Start each new line near to the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien exact horizontal position
        self.x = float(self.rect.x)

