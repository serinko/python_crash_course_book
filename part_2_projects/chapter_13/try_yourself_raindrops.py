import sys
import pygame
from pygame.sprite import Sprite


class RainDrop(Sprite):
    def __init__(self, StarSky):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = StarSky.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/a_star.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


class Settings():
    def __init__(self):
        # self.screen_width = 1920
        # self.screen_height = 1060
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.bg_color = (0, 17, 26,)
        # Ship settings
        # Setting the speed like this will make much easier to change it later
