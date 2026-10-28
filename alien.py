import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent aliens' fleet"""

    def __init__(self, alien_invasion):
        super().__init__() #Import Sprite methods and attributes 
        self.SHIP_SIZE = (50,50)

        self.screen = alien_invasion.screen # Get screen surface object from alien invasion instance

        #Load the alien's ship image
        self.image_left = pygame.Surface.convert_alpha(pygame.image.load("./images/Alien_Space_Ship_Left.png")) 
        self.image_right = pygame.Surface.convert_alpha(pygame.image.load("./images/Alien_Space_Ship_Right.png")) 


        self.alien_ship_left = pygame.transform.scale(self.image_left,self.SHIP_SIZE)
        self.alien_ship_right = pygame.transform.scale(self.image_right,self.SHIP_SIZE)


        # Operate with the same rectangle 
        self.ship_rect = self.alien_ship_left.get_rect()

        self.ship_rect.x = self.ship_rect.width
        self.ship_rect.y = self.ship_rect.height

        self.x = float(self.ship_rect.x)
        

