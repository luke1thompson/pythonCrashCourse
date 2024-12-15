import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""
    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.center_ship()
        
        # Movement flags, by default the ship is not moving
        self.moving_r = False
        self.moving_l = False
        
    def update(self):
        """Update the ships position based on the moving flag"""
        # checks if the flag is set AND the ship image is located onscreen
        if self.moving_r and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_l and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
        
    def center_ship(self):
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)