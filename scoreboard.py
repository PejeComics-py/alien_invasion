import pygame.font 
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Keep track player's score"""
    def __init__(self, alien_invasion):
        """Intilize class viarables"""
        # Initilizing variables declared in alien_invasion module
        self.alien_invasion = alien_invasion
        self.screen = alien_invasion.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = alien_invasion.game_settings
        self.stats = alien_invasion.stats

        # Text color en import system font
        self.text_color = (8, 8, 8)
        self.font = pygame.font.SysFont(None,48)

        # Preape score text
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score variable into an image"""
        rounded_score = round(self.stats.score, -1)
        self.score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.settings.SCREEN_COLOR)

        # Get rect image and move the right top
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn high score into an image"""
        rounded_score = round(self.stats.high_score,-1)
        self.hs_str = f"{rounded_score:,}"
        self.hs_image = self.font.render(self.hs_str,True, self.text_color,self.settings.SCREEN_COLOR)

        self.hs_rect = self.hs_image.get_rect()
        self.hs_rect.centerx = self.screen_rect.centerx
        self.hs_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn current level text into image"""
        self.level_str = f"level: {self.stats.level}"
        self.level_image = self.font.render(self.level_str, True, self.text_color, self.settings.SCREEN_COLOR)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many lives the player has"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_lives):
            ship = Ship(self.alien_invasion)
            # Move the ship images one rectangle width 
            ship.rect.x = 10 + (ship_number * ship.rect.width * 2)
            ship.rect.y = self.score_rect.top
            self.ships.add(ship)

    def show_score(self):
        """Display score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hs_image, self.hs_rect)
        self.screen.blit(self.level_image, self.level_rect)
        for ship in self.ships.copy():
            self.screen.blit(ship.human_ship,ship.rect)

    def check_high_score(self):
        """Check if current score is the highest"""
        if self.stats.high_score < self.stats.score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
