class GameStats:
    def __init__(self,alien_invasion):
        """Class to save game stats"""
        self.settings = alien_invasion.game_settings
        self.__reset_stats()

    def __reset_stats(self):
        # Instanciate game stats
        self.ships_lives = self.settings.SHIP_LIMIT
