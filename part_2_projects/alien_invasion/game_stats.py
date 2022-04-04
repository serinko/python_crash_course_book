import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        # High score should never be reset
        self.high_score = self._get_saved_high_score()

        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_saved_high_score(self):
        """json file with storing top score as and integer"""
        filename = 'high_score.json'
        try:
            with open(filename) as f:
                saved_score = f.read(json.load(f))

        except FileNotFoundError:
            with open(filename, 'w') as f:
                # Initiating a block to work with file as f ('w' for write)
                saved_score = 0
                json.dump(saved_score, f)
            return saved_score
        else:
            return saved_score

    def _check_saved_high_score(self, ):
        """Prompt for a new username"""
        prompt = "Hello, please enter your username:  "
        username = input(prompt)
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
        return username
        # This function prompts new user name and gets called for by
        # greet_user only if the stored_user_name does not exist
