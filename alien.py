import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent aliens' fleet"""

    def __init__(self, alien_invasion):
        super().__init__() #Import Sprite methods and attributes 
        self.SHIP_SIZE = (40,30)

        self.screen = alien_invasion.screen # Get screen surface object from alien invasion instance

        #Load the alien's ship image
        self.image = pygame.Surface.convert_alpha(pygame.image.load("./images/alien.png")) 

        self.image = pygame.transform.scale(self.image,self.SHIP_SIZE)

        # Operate with the same rectangle 
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        

