import pygame.font

class Button:
    """It's a button, stupid"""
    def __init__(self, game, msg) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        """Dimensions and properties"""
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        """Build a Rect"""
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        """Prep message, just once"""
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turns msg into a rendered image with centered text"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)