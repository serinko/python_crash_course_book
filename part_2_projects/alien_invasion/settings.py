# import pygame
import random as r


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1060
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.bg_color = (0, 17, 26,)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = r.randrange(15, 40)
        self.bullet_color = (255, 255, 255,)
        self.bullets_allowed = 20

        # Alien settings
        self.fleet_drop_speed = 20

        # How quickly the fleet speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize setting that change during the game"""

        # Setting the speed like this will make much easier to change it later
        self.ship_speed = 7

        self.bullet_speed = 5
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
