class GameStats:
    def __init__(self,alien_invasion):
        """Class to save game stats"""
        self.settings = alien_invasion.game_settings
        self.reset_stats()

    def reset_stats(self):
        # Instanciate and reset game stats
        self.ships_lives = self.settings.SHIP_LIMIT
        self.settings.bullet_speed = 15.0
        self.settings.alien_speed = 2.5 

