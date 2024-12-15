import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bul_color
        
        # Create a bullet rect at (0,0) and then set correct pos
        self.rect = pygame.Rect(0, 0, self.settings.bul_width, self.settings.bul_height)
        self.rect.midtop = game.ship.rect.midtop
        
        # Store the bullets y pos as a float
        self.y = float(self.rect.y)
        self.image = pygame.image.load('images/alien.bmp')
        
    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bul_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
class Piercer(Bullet):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(0,0, self.settings.p_width, self.settings.p_height)
        self.rect.midtop = game.ship.rect.midtop
        
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.p_speed
        self.rect.y = self.y
        
    def draw_piercer(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
class Bomb(Bullet):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.game = game
        self.color = (230, 0, 0)
        self.rect = pygame.Rect(0,0, self.settings.b_width, self.settings.b_height)
        self.rect.midtop = self.game.ship.rect.midtop
        
        self.y = float(self.rect.y)
        
        self.boom_image = pygame.image.load('images/explode.bmp')
        self.boom_rect = self.boom_image.get_rect()
        self.lingering = False
        self.linger_timer = 100
        
    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.b_speed
        self.rect.y = self.y
        
    def draw_bomb(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def shoot(self):
        self.rect.midtop = self.game.ship.rect.midtop
        
    def explode(self):
        self.rect.width = 200
        self.rect.height = 200
        self.rect.center = self.rect.topleft
        
    def linger(self):
        if not self.lingering:
            self.lingering = True
            self.boom_rect.center = self.rect.center
        else:
            self.linger_timer -= 1

    def draw_boom(self):
        self.screen.blit(self.boom_image, self.boom_rect)