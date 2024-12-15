class GameStats:
    """Track statistics for AlieNvasion"""

    def __init__(self, game) -> None:
        self.settings = game.settings
        self.high_score = 0
        self.reset_stats()
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        