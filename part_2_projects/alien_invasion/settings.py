# import pygame
import random as r
import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1060
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.bg_color = (0, 17, 26,)
        # Ship settings
        # Setting the speed like this will make much easier to change it later
        self.ship_speed = 7

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = r.randrange(15, 40)
        self.bullet_color = (255, 255, 255,)
        self.bullets_allowed = 20

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
