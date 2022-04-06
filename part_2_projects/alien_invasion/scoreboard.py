import pygame.font
from pygame.sprite import Group

from ship import ShipSB


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.text_color = (245, 208, 0)
        self.font = pygame.font.SysFont('Helvetica', 60)

        # Prepare the initial score for the game
        self.prep_score()
        self.prep_high_score()
        self.prep_top_player()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""

        rounded_score = round(self.stats.score, -1)
        # If you round the value to negative, round() function
        # rounds up to the nearest 10, 100, 1000 etc
        score_str = "{:,}".format(rounded_score)
        # Adds a comma to the string number format
        label = "Score: "
        scr_str = f"{label}{score_str}"

        self.score_image = self.font.render(
            scr_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Display the score ath the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores. level and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.top_pl_image, self.tp_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        # high_score = round(self.stats.high_score, -1)
        # high_score_str = "{:,}".format(high_score)

        high_score = round(self.stats.high_score, -1)

        label = "High Score: "
        h_s_str = f"{label}{high_score}"
        self.high_score_image = self.font.render(
            h_s_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        # Matching the top alignment of the score

    def prep_top_player(self):
        top_pl = self.stats.get_top_player()
        label = "player: "
        tp_str = f"[{top_pl}]"
        self.top_pl_image = self.font.render(
            tp_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        self.tp_rect = self.top_pl_image.get_rect()
        self.tp_rect.left = self.high_score_rect.right + 20
        self.tp_rect.top = self.score_rect.top
        # Matching the top alignment of the score

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.new_top_user = self.stats.user

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        label = "Level: "
        lvl_str = f"{label}{level_str}"
        self.level_image = self.font.render(
            lvl_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Position of the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        # creates an empty group [list]
        for ship_number in range(self.stats.ships_left):
            ship = ShipSB(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
