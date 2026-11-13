class GameStats:
    def __init__(self,alien_invasion):
        """Class to save game stats"""
        self.settings = alien_invasion.game_settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        # Instanciate and reset game stats
        self.ships_lives = self.settings.SHIP_LIMIT
        self.score = 0
        self.level = 1
        self.settings.bullet_speed = self.settings.BASE_BULLET_SPEED
        self.settings.alien_speed = self.settings.BASE_ALIEN_SPEED
        self.settings.alien_points = self.settings.BASE_ALIEN_POINTS  

