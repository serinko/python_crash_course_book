# Try It Yourse lf
# 12-5. Sideways Shooter: Write a game that places a ship on the left side of
# the screen and allows the player to move the ship up and down.
# Make the ship fire a bullet that travels right across the screen
# when the player presses the spacebar.
# Make sure bullets are deleted once they disappear off the screen.

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Run he game in fulscreen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # run it pre set default screen
        # self.screen = pygame.display.set_mode((
        #     self.settings.screen_width, self.settings.screen_height
        # ))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Set the background color
        self.bg_color = (0, 17, 26)

    def run_game(self):
        """Start the maiu loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        # _method() is known as a helper method
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
