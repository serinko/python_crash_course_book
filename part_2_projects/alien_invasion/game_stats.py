import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        # High score should never be reset
        self.high_score = self.get_high_score()
        self.user = self.get_username()

        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an inactive state
        self.game_active = False

    def get_username(self):
        msg = \
            '\n\nHello, welcome to Alien Invasion. A study simple game project.' \
            ' Before you start please enter your name. To quit the game press ' \
            '"Q", to restart press "R".' \
            ' \n\n   ---------------------------------------   '
        prompt = '\n\nUSERNAME: '
        print(msg)
        self.username = input(prompt)
        return self.user

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
            if value:

                return value
            else:
                with open(filename, 'w') as f:
                    saved_hc = {self.user: 0}
                    json.dump(saved_hc, f)

                return saved_hc[self.user]

        # except FileNotFoundError:
        #     with open(filename, 'w') as f:
        #         # Initiating a block to work with file as f ('w' for write)
        #         saved_hc = {self.user:0}
        #         json.dump(saved_hc, f)
        #
        #         print(f"xcept {saved_hc}")
        #         for i in saved_hc:
        #         return self.user[i]
        #
        # else:
        #     if self.user[i]:
        #   #  if saved_score:
        #         return self.user[i]
        #     else:
        #         with open(filename, 'w') as f:
        #             saved_score = 0
        #             json.dump(saved_score, f)
        #
        #         return saved_score

    def store_high_score(self, saved_score):
        """Overwrite new highscore"""

        filename = 'high_score.json'
        new_h_c = round(self.high_score, -1)
        new_h_c = int(new_h_c)
        with open(filename, 'w') as f:
            json.dump(new_h_c, f)
        print(f"savedscore {new_h_c}")
    #
    # def save_name(self):
    #     """
