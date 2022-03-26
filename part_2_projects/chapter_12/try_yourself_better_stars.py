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
