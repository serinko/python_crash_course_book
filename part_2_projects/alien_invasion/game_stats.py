import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        # High score should never be reset
        self.user = self.get_username()
        self.high_score = self.get_high_score()
        self.top_pl = self.get_top_player()

        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an inactive state
        self.game_active = False

    def get_username(self):
        msg = \
            '\n\nHello, welcome to Alien Invasion. A study simple game project.' \
            ' Before you start please enter your name. To quit the game press ' \
            '"Q", to restart press "R".' \
            ' \n\n---------------------------------------   '
        prompt = '\nUSERNAME: '
        print(msg)
        user = input(prompt)
        return user

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        """json file with storing top score as and integer"""
        filename = 'high_score.json'

        with open(filename) as f:
            saved_hc = json.load(f)

        for user, value in saved_hc.items():
            return value

    def get_top_player(self):
        """Get the the high score saved player."""
        filename = 'high_score.json'

        with open(filename) as f:
            saved_hc = json.load(f)

        for user, value in saved_hc.items():
            # if value:
            return user

    def store_high_score(self, top_player):
        """Overwrite new highscore"""

        filename = 'high_score.json'
        high_score = round(self.high_score, -1)
        # new_hc = int(new_hc)
        self.usr_hc = {top_player: high_score}
        with open(filename, 'w') as f:
            json.dump(self.usr_hc, f)

    def _compare_top_player(self):
        """Function checking if the current player is the best player."""
        if self.top_pl == self.user:
            True

    def exit_message(self):
        """Prints exit message"""
        print("\n\n\n---------------------------------------   ")
        msg_1 = f"\nTOP SCORE: "
        msg_2 = "\nCONGRATULATIONS ! ! !\nYou made a new TOP SCORE:
        if self._compare_top_player():
            print(msg_2)
        else:
            print(msg_1)

        for key, value in self.usr_hc.items():
            print(f"{key} - {value}! ")

        print("\nHave a nice day <3")
   