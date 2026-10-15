import sys  # Module to interact with the system
import pygame  # Module to create games 

class AlienInvasion:
    """Class to manage game assets and behavior"""
    def __init__(self):
        """Initilizing pygame necessary pygame modules"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
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

if __name__ == "__main__":
    """Check if game is running as a script"""
    game_instance = AlienInvasion() 
    game_instance.run_game()
