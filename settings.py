class Settings:
    """Class to operate settings for Alien Invasion"""
    def __init__(self): 
        # General settings
        self.SCREEN_RESOLUTION = (1200,800) 
        self.SCREEN_COLOR = (230,230,230)
        self.FPS = 24
        self.BASE_SPEED = 20.0
        self.SPEED_LIMIT = 25.0
        self.current_speed = self.BASE_SPEED

        # Bullet properties
        self.BULLET_SPEED = 15.0
        self.BULLET_WIDTH = 3
        self.BULLET_HEIGHT = 15
        self.BULLET_COLOR = (60, 60, 60)
        self.BULLET_LIMIT = 3 

