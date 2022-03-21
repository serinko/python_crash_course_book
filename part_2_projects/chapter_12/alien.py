import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    "A Class to represent single alien in the fleet"

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen