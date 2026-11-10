import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent aliens' fleet"""
    def __init__(self, alien_invasion):
        super().__init__() #Import Sprite methods and attributes 
        self.ALIEN_SIZE = (47.5,37.5)

        self.settings = alien_invasion.game_settings
        self.screen = alien_invasion.screen # Get screen surface object from alien invasion instance


        #Load the alien's ship image
        self.image = pygame.Surface.convert_alpha(pygame.image.load("./images/alien.png")) 

        self.image = pygame.transform.scale(self.image,self.ALIEN_SIZE)

        # Operate with the same rectangle 
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """ Check if one alien instance is at edge of screen """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0) 

    def update(self):
        """Move the alien to right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
