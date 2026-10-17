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
                #running = False # Probably this variable is not needed 
                sys.exit(0)
    

    def __update_screen(self):
        self.screen.fill(self.screen_color) # Function a fills a color to surface object
            
        self.clock.tick(self.game_settings.FPS) 
            
        self.ship.draw_me() # Draw the ship

        pygame.display.flip() # According to some Wikis, this enable graphics rendering 

if __name__ == "__main__":
    """Check if game is running as a script"""
    game_instance = AlienInvasion() 
    game_instance.run_game()
