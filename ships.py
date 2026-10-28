import pygame

class Ship:
    """Class to manage ship propeties"""
    def __init__(self, alien_invasion):
        self.SHIP_SIZE = (50,50)
        self.screen = alien_invasion.screen # Assing variable screen value of surface created
        self.screen_rectangle = alien_invasion.screen.get_rect() # Rectangle of the screen for collisions Note: Apperently this helps for positioning

        self.image = pygame.Surface.convert_alpha(pygame.image.load("./images/human_space.png")) # Load image
        self.human_ship = pygame.transform.scale(self.image,self.SHIP_SIZE)
        
        self.ship_rectangle = self.human_ship.get_rect() # Get Rectangle of pygame image object
        self.ship_rectangle.midbottom = self.screen_rectangle.midbottom # Make the ship's midbottom position equal to the screen's midbottom
    def draw_me(self):
        self.screen.blit(self.human_ship,self.ship_rectangle) # Draw image surface
   
