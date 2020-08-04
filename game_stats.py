class GameStats:
    """ Track statics for Alien Invasion"""

    def __init__(self, ai_game):
        """ Inialize statics."""
        self.setting = ai_game.setting
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """ Inializs statics that can change during the game"""
        self.ship_left = self.setting.ship_limit
        self.score= 0