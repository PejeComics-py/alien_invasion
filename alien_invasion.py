import sys  # Module to interact with the system
import pygame  # Module to create games 
from settings import Settings 
from ships import Ship

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

    def run_game(self):
        """Start main loop for game"""
        # running = True
        while True:
            self.__check_events() #Responde to user's input
            self.__update_screen()
            
    def __check_events(self):
        """Respond to inputs events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit(0)
        self.__key_events()
       
    def __update_screen(self):
        self.screen.fill(self.screen_color) # Function a fills a color to surface object
            
        self.clock.tick(self.game_settings.FPS) 
            
        self.ship.draw_me() # Draw the ship

        pygame.display.flip() # According to some Wikis, this enable graphics rendering 

        self.ship.ship_rectangle.clamp_ip(self.ship.screen_rectangle) # Ensure ship surface stays inside screen's rectangle
  
    def __key_events(self):
        """Movement of ship"""
        keys = pygame.key.get_pressed() # Get boolean dictionary of states of keys in keyboard
        # Logic for moving right 
        if keys[pygame.K_RIGHT] is True:
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.ship_rectangle.x += self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.x += self.game_settings.SPEED_LIMIT
        # Logic for moving left
        elif keys[pygame.K_LEFT] is True:
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.ship_rectangle.x -=self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.x -= self.game_settings.SPEED_LIMIT
        # Logic for moving up 
        elif keys[pygame.K_UP] is True:
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT: 
                self.ship.ship_rectangle.y -=self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.y -= self.game_settings.SPEED_LIMIT
        # Logic for moving down
        elif keys[pygame.K_DOWN] is True:
            if self.game_settings.current_speed < self.game_settings.SPEED_LIMIT:
                self.ship.ship_rectangle.y +=self.game_settings.current_speed
                self.game_settings.current_speed *=1.05
            else: 
                self.ship.ship_rectangle.y += self.game_settings.SPEED_LIMIT
        # Resetting movement speed when a key not key is being pressed
        else:
            self.game_settings.current_speed = self.game_settings.BASE_SPEED

if __name__ == "__main__":
    """Check if game is running as a script"""
    game_instance = AlienInvasion() 
    game_instance.run_game()
