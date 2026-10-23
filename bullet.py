import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage game's bullets"""
    def __init__(self, alien_invasion):
        """Handling bullet initialization"""
        super().__init__()
        self.screen = alien_invasion.screen
        self.settings = alien_invasion.game_settings
        self.color = self.settings.BULLET_COLOR 
        
        # Instantiating rect object at position 0,0
        self.bullet_rect = pygame.Rect(0,0,self.settings.BULLET_WIDTH, self.settings.BULLET_HEIGHT)
        # Change position at midtops ship 
        self.bullet_rect.midtop = alien_invasion.ship.ship_rectangle.midtop

        # Store y coordinates of rect object 
        self.y = float(self.bullet_rect.y)
    def update(self):
        """Bullet's movement"""
        self.y -= self.settings.BULLET_SPEED 
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet"""
        pygame.draw.rect(self.screen,self.color,self.bullet_rect)
