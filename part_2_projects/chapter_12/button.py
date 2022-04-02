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

    def _prep_message(self, msg):
        """Turn mag into a rendered image and center text on the button."""

        self.msg_image = self.font.render(
            msg, True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw a message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # fill() is called to draw recctangular portion of the button
        # blit() to draw text image oin the screen
