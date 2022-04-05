import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        # High score should never be reset
        self.high_score = self.get_saved_high_score()

        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_saved_high_score(self):
        """json file with storing top score as and integer"""
        filename = 'high_score.json'
        try:
            with open(filename) as f:
                saved_score = f.read(json.load(f))
                if saved_score:
                    return saved_score

        except FileNotFoundError:
            with open(filename, 'w') as f:
                # Initiating a block to work with file as f ('w' for write)
                saved_score = 0
                json.dump(saved_score, f)

                print(saved_score)
                return saved_score

    def _check_saved_high_score(self):
        """Compare the saved and current high score and save the higher"""
        if self.high_score > saved_h_c:
            new_h_c = round(self.high_score, -1)
            self._store_new_high_score(new_h_c)

    def store_new_high_score(self, saved_score):
        """Overwrite new highscore"""

        filename = 'high_score.json'
        if saved_score:
            if self.high_score > saved_score:
                new_h_c = round(self.high_score, -1)
                with open(filename, 'r+') as f:
                    json.dump(new_h_c, f)
                return new_h_c
        else:
            new_h_c = round(self.high_score, -1)
            with open(filename, 'r+') as f:
                json.dump(new_h_c, f)
            return new_h_c

