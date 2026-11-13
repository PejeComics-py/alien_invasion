#!./venv/bin/python

import sys  # Module to interact with the system
import pygame  # Module to create games 
from settings import Settings 
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard

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

        # Dedicated game objects 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()    
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Start alien invasion bool
        self.game_active = False
        self.__create_fleet()

        # Buttons and UI menu
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start main loop for game"""
        # running = True
        while True:
            self.__update_screen() #Update screen 
            if self.game_active:
                self.__update_bullets() #Control bullets instances
                self.__update_aliens()
                self.__check_game_events() #Respond to user's input
            else: 
                self.__check_system_events()
            
    def __check_game_events(self):
        """Respond to inputs events after game_active = True"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Shoot pew pew 
                    self.__fire_bullet()
                if event.key == pygame.K_q: 
                    sys.exit(0)
        self.__key_events()

    def __check_system_events(self):
        """Respond to user's input before game start"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.__check_play_button(mouse_pos)

    def __check_play_button(self, pos):
        """Check if mouse position is over play_button rectangle"""
        button_clicked = self.play_button.rect.collidepoint(pos)
        if button_clicked and not self.game_active:
            pygame.mouse.set_visible(False)
            self.game_active = True
       
    def __update_screen(self):
        """Update screen events"""
        self.screen.fill(self.screen_color) # Function a fills a color to surface object

        if self.game_active:  
            self.sb.prep_ships()
            self.sb.show_score()
               
        if self.game_active:
            self.ship.draw_me() # Draw the ship
            for bullet in self.bullets.sprites(): #Order is important, needs to draw rectangle before flip()
                bullet.draw_bullet()
            self.aliens.draw(self.screen)

        # Draw the play button 
        if not self.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip() # According to some Wikis, this enable graphics rendering 

        self.clock.tick(self.game_settings.FPS) #Limit games fps

        self.ship.rect.clamp_ip(self.ship.screen_rectangle) # Ensure ship surface stays inside screen's rectangle
        

    def __update_bullets(self):
        """Update the bullet properties"""
        self.bullets.update()
        self.__remove_bullet()
        self.__check_bullet_collisions()
        # Updates level scaling and level
        if len(self.aliens) == 0:
            self.stats.level += 1
            self.sb.prep_level()
            self.__reset()
            self.game_settings.initilialize_dynamic_settings()

    def __check_bullet_collisions(self):
        """Kill aliens with pew pew"""
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.game_settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def __reset(self):
        """ Reset game """
        self.bullets.empty()
        self.aliens.empty()
        # Create new fleet and center ship
        self.ship.center_ship()
        self.__create_fleet()

    def __remove_bullet(self):
        """Remove the bullet"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
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
        current_x,current_y = alien_width, 100
        screen_resolution = list(self.game_settings.SCREEN_RESOLUTION)
        screen_width,screen_height = screen_resolution

        # Loops to control alien generation in x and y
        while current_y < (screen_height / 2):
            while current_x < (screen_width - (2 * alien_width)):
                
                # Create alien instance and move 2 times the alien width
                self.__create_alien(current_x,current_y)
                current_x += 2 * alien_width

            # Reset current_x to start new row
            current_x = alien_width
            current_y += 2 * alien_height
    
    def __update_aliens(self):
        """Update the aliens position"""
        self.__check_fleet_edges()
        self.aliens.update()
        self.__check_ship_alien_collisions()

    def __check_ship_alien_collisions(self):
        """Check alien on ship collision"""
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.__ship_hit()
        # If an alien touch the bottom screen, you lose
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().height:
                self.__ship_hit()
                break

    def __ship_hit(self):
        """ Respond when ship is hit"""
        # Reduce ship lives
        self.stats.ships_lives -= 1
        self.sb.prep_ships()

        if self.stats.ships_lives > 0:
            # Reset game
            self.__reset()
            sleep(0.25)
        else:
            self.game_active = False 
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.__reset()
            pygame.mouse.set_visible(True)

    def __create_alien(self, x, y):
        """ Create new alien instance """
        new_alien = Alien(self)
        new_alien.x = x
        # This is the important parameter to move alien position
        new_alien.rect.x = x
        new_alien.rect.y = y
        self.aliens.add(new_alien)

    def __check_fleet_edges(self):
        """Check if fleet has reached the edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.__change_fleet_direction()
                break
    def __change_fleet_direction(self):
        """Drop the entire fleet and change its position"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.game_settings.FLEET_DROP_SPEED
        # Inverse direction without using if statements, actually genius
        self.game_settings.fleet_direction *= -1 

    def __key_events(self):
        """Movement of ship and other functionalities"""
        keys = pygame.key.get_pressed() # Get boolean dictionary of states of keys in keyboard
        if keys[pygame.K_RIGHT] is True:
            # Logic for moving right 
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.rect.x += self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.rect.x += self.game_settings.SPEED_LIMIT
        elif keys[pygame.K_LEFT] is True:
            # Logic for moving left
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.rect.x -=self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.rect.x -= self.game_settings.SPEED_LIMIT
        else:
            # Resetting movement speed when a key not key is being pressed
            self.game_settings.current_speed = self.game_settings.BASE_SPEED

if __name__ == "__main__":
    """Check if game is running as a script"""
    game_instance = AlienInvasion() 
    game_instance.run_game()
