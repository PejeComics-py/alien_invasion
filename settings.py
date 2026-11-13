class Settings:
    """Class to operate settings for Alien Invasion"""
    def __init__(self): 
        # General settings
        self.SCREEN_RESOLUTION = (1200,800) 
        self.SCREEN_COLOR = (230,230,230)
        self.FPS = 24
        self.GAME_SCALING = 1.2 
        self.SCORE_SCALE = 1.2
        
        # Bullet properties
        self.BASE_BULLET_SPEED =  15.0
        self.bullet_speed = 15.0
        self.BULLET_WIDTH = 4.5
        self.BULLET_HEIGHT = 15
        self.BULLET_COLOR = (60, 60, 60)
        self.BULLET_LIMIT = 10

        # Alien properties
        self.BASE_ALIEN_SPEED = 2.5
        self.alien_speed = 2.5 
        # Fleet direction 1=right | 2=left
        self.fleet_direction = 1 
        self.FLEET_DROP_SPEED = 10
        self.BASE_ALIEN_POINTS = 50
        self.alien_points = 50

        # SHIP properties
        self.BASE_SPEED = 25.0
        self.SPEED_LIMIT = 45.0
        self.current_speed = self.BASE_SPEED
        self.SHIP_LIMIT = 3

    def initilialize_dynamic_settings(self):
        self.bullet_speed = self.bullet_speed * self.GAME_SCALING
        self.alien_speed = self.alien_speed * self.GAME_SCALING
        self.alien_points = int(self.alien_points * self.SCORE_SCALE)

