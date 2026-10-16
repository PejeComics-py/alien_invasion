import sys  # Module to interact with the system
import pygame  # Module to create games 
from settings import Settings 

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
    def run_game(self):
        """Start main loop for game"""
        # running = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #running = False # Probably this variable is not needed 
                    sys.exit(0)
            pygame.display.flip() # According to some Wikis, this enable graphics rendering 
            self.screen.fill(self.screen_color) # Function a fills a color to surface object
            self.clock.tick(self.game_settings.FPS) 

if __name__ == "__main__":
    """Check if game is running as a script"""
    game_instance = AlienInvasion() 
    game_instance.run_game()
