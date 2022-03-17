"""Module for simple setting overview of alien_1"""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1060

        self.bg_color = (0, 17, 26,)
        # Ship settings
        # Setting the speed like this will make much easier to change it later
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255,)
        self.bullets_allowed = 8
