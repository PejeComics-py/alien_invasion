import pygame.font

class Button:
    """ Class to make game buttons """
    def __init__(self, alien_invasion, msg):
        self.screen = alien_invasion.screen
        self.screen_rect = self.screen.get_rect()

        # Font paramenters
        self.width, self.height, self.button_color = 200, 50, (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # Let build the button 
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.__print_msg(msg)

    def __print_msg(self, msg):
        """ Turn any string into a button and render to the screen """
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw the button and bg rec"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



