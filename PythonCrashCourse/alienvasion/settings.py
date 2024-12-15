import pygame

class Settings:
    """A class for storing settings for Alienvasion"""

    def __init__(self) -> None:
        """Screen settings"""
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.ship_limit = 3
        
        
        """Bullet settings"""
        self.bul_width = 10
        self.bul_height = 20
        self.bul_color = (60, 60, 60)
        self.bul_max = 3
        
        """Alien settings"""
        # self.alien_downframes = 20
        
        """Special bullet settings"""
        self.p_width = 50
        self.p_height = 10
        self.p_speed = 2.5
        self.p_max = 10
        
        """bomb settings"""
        self.b_active = False
        self.b_speed = 2.0
        self.b_timer = 240
        self.b_width = 10
        self.b_height = 10
        
        self.speed_scaling = 1.3
        self.score_scaling = 1.5
        
        self.initialize_dynamics()
        
    def initialize_dynamics(self):
        self.ship_speed = 4.0
        self.bul_speed = 6.0
        self.alien_speed = 2.0
        self.alien_downframes = 30
        
        self.alien_points = 50
        
    def increase_speed(self):
        self.ship_speed *= self.speed_scaling
        self.bul_speed *= self.speed_scaling
        self.alien_speed *= self.speed_scaling
        self.alien_points = int(self.alien_points * self.score_scaling)
        self.alien_downframes -= 2