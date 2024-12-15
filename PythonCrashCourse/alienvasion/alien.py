import pygame

# from pathlib import Path
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage the enemies"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
  
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.direction = 1
        self.next_dir = 0
        self.downframes = self.settings.alien_downframes
        
        # Start the alien near the origin, accounting for image size
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.x)
        
    def update(self):
        if (self._at_edge()) and (self.next_dir == 0):
            self.next_dir = -1 * self.direction
            self.direction = 0
        elif (self.direction == 0) and (self.downframes > 0):
            self.rect.y += self.settings.alien_speed
            self.downframes -= 1
        elif self.downframes <= 0:
            self.direction = self.next_dir
            self.next_dir = 0
            self.rect.x += self.settings.alien_speed * self.direction
            self.downframes = self.settings.alien_downframes
        else:
            self.rect.x += self.settings.alien_speed * self.direction
        
    def _at_edge(self):
        """Return True if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left < 0)

