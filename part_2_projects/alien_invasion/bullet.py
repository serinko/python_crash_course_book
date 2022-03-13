import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
    """Create a bullet object at the ship's current position"""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    