import pygame.font


class Buton:

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (255, 178, 36)
        self.text_color = (224, 176, 255)
        self.font = pygame.font.SysFont('Helvetica', 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.center)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only ones
        self._prep_message(msg)

        