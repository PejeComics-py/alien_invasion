#!/usr/bin/python

import sys  # Module to interact with the system
import pygame  # Module to create games 
from settings import Settings 
from ships import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Class to manage game assets and behavior"""
    def __init__(self):
        """Initilizing pygame necessary pygame modules"""
        pygame.init()
        self.game_settings = Settings() # Create settings objects
        self.screen = pygame.display.set_mode(self.game_settings.SCREEN_RESOLUTION) # Create and initialize surface object
        self.clock = pygame.time.Clock() # Create object clock object 
        self.screen_color = (self.game_settings.SCREEN_COLOR)
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()    
        
        self.__create_fleet()

    def run_game(self):
        """Start main loop for game"""
        # running = True
        while True:
            self.__check_events() #Respond to user's input
            self.__update_screen() #Update screen 
            self.__update_bullets() #Control bullets instances
            
    def __check_events(self):
        """Respond to inputs events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit(0)
                if event.key == pygame.K_SPACE:
                    # Shoot pew pew 
                    self.__fire_bullet()
        self.__key_events()
       
    def __update_screen(self):
        """Update screen events"""
        self.screen.fill(self.screen_color) # Function a fills a color to surface object
               
        self.ship.draw_me() # Draw the ship

        for bullet in self.bullets.sprites(): #Order is important, needs to draw rectangle before flip()
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        
        pygame.display.flip() # According to some Wikis, this enable graphics rendering 

        self.clock.tick(self.game_settings.FPS) #Limit games fps

        self.ship.ship_rectangle.clamp_ip(self.ship.screen_rectangle) # Ensure ship surface stays inside screen's rectangle
        

    def __update_bullets(self):
        """Update the bullet properties"""
        self.bullets.update()
        self.__remove_bullet()

    def __remove_bullet(self):
        """Remove the bullet"""
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def __fire_bullet(self):
        """Create bullet and add it to group"""
        if len(self.bullets) < self.game_settings.BULLET_LIMIT:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def __create_fleet(self):
        """Create aliens' fleet at correct position"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien.rect.height
        
        # Get screen properties
        current_x,current_y = alien_width, alien_height
        screen_resolution = list(self.game_settings.SCREEN_RESOLUTION)
        screen_width,screen_height = screen_resolution

        # Loops to control alien generation in x and y
        while current_y < ((screen_height / 2) - (4 * alien_height)):
            while current_x < (screen_width - (2 * alien_width)):
                
                # Create alien instance and move 2 times the alien width
                self.__create_alien(current_x,current_y)
                current_x += 2 * alien_width

            # Reset current_x to start new row
            current_x = alien_width
            current_y += 2 * alien_height
    
    def __create_alien(self, x, y):
        """ Create new alien instance """
        new_alien = Alien(self)
        new_alien.x = x
        # This is the important parameter to move alien position
        new_alien.rect.x = x
        new_alien.rect.y = y
        self.aliens.add(new_alien)


    def __key_events(self):
        """Movement of ship and other functionalities"""
        keys = pygame.key.get_pressed() # Get boolean dictionary of states of keys in keyboard
        if keys[pygame.K_RIGHT] is True:
            # Logic for moving right 
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.ship_rectangle.x += self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.x += self.game_settings.SPEED_LIMIT
        elif keys[pygame.K_LEFT] is True:
            # Logic for moving left
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.ship_rectangle.x -=self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.x -= self.game_settings.SPEED_LIMIT
        elif keys[pygame.K_UP] is True:
            # Logic for moving up 
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.ship_rectangle.y -=self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.y -= self.game_settings.SPEED_LIMIT
        elif keys[pygame.K_DOWN] is True:
            # Logic for moving down
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT:
                self.ship.ship_rectangle.y +=self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.y += self.game_settings.SPEED_LIMIT
        else:
            # Resetting movement speed when a key not key is being pressed
            self.game_settings.current_speed = self.game_settings.BASE_SPEED

if __name__ == "__main__":
    """Check if game is running as a script"""
    game_instance = AlienInvasion() 
    game_instance.run_game()
