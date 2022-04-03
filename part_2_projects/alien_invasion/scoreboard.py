import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
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
        self.prep_level()

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
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        label = "High Score: "
        h_s_str = f"{label}{high_score_str}"
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

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

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
