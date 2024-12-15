import sys
from pathlib import Path

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet, Piercer, Bomb
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class Alienvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self) -> None:
        pygame.init()
        
        """Prepping and clearing the log file"""
        self.path = Path("alienlog.txt")
        self.path.write_text("")
        
        self.settings = Settings()
        self.screen = self.settings.screen
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("AlieNvasion")
        self.button = Button(self, "Play")
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        
        # Create the ship and bulletgroup
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.piercers = pygame.sprite.Group()
        self.bomb = Bomb(self)
        self.aliens = pygame.sprite.Group()
        
        self.game_active = False
        
        self._create_fleet()
        
    def run_game(self):
        # pygame.time.delay(2000)
        
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_projectiles()
                self._update_aliens()
            
            self._update_screen()

            self.clock.tick(60)
            
    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(pygame.mouse.get_pos())
    
    def _check_keydown(self, event):
        """respond to keydown events"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_r = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_l = True
        elif event.key == pygame.K_SPACE:
            self._shoot_bullet()
        elif event.key == pygame.K_v:
            self._shoot_piercer()
        elif event.key == pygame.K_b:
            self._shoot_bomb()
            
    def _check_keyup(self, event):
        """respond to keyup events, allowing smooth movement when key is held"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_r = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_l = False
            
    def _check_play_button(self, mouse):
        """Start the game when the player clicks the button"""
        if self.button.rect.collidepoint(mouse) and not self.game_active:
            self.game_active = True
            pygame.mouse.set_visible(False)
            self.scoreboard.prep_ships()
            self.scoreboard.prep_level()
            self.stats.reset_stats()
            self._reset()
    
    def _update_screen(self):
        """Update images and objects on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()
        
        for bullet in self.bullets:
            bullet.draw_bullet()
        for piercer in self.piercers:
            piercer.draw_piercer()
        if self.settings.b_active:
            self.bomb.draw_bomb()
        elif self.bomb.lingering:
            self.bomb.draw_boom()
        
        if not self.game_active:
            self.button.draw_button()
        
        pygame.display.flip()
        
    def _shoot_bullet(self):
        if len(self.bullets) < self.settings.bul_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _shoot_piercer(self):
        if len(self.piercers) < self.settings.p_max:
            new_piercer = Piercer(self)
            self.piercers.add(new_piercer)
    
    def _shoot_bomb(self):
        if not self.settings.b_active:
            self.settings.b_active = True
            self.bomb.shoot()
        
    def _update_projectiles(self):
        self.bullets.update()
        self.piercers.update()
        if self.settings.b_active:
            self.bomb.update()
        
        """Remove bullets that are above the top of the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        for piercer in self.piercers.copy():
            if piercer.rect.bottom <= 0:
                self.piercers.remove(piercer)
                
        """Check collisions"""
        bhit = self._check_bullet_collisions()
        phit = self._check_piercer_collisions()
        ehit = self._check_bomb_exploding()
        if bhit or phit or ehit:
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()
        
        """Reset all sprites and respawn fleet if no aliens"""
        if not self.aliens:
            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()
            self._reset()
            
    def _reset(self):
        self.bullets.empty()
        self.piercers.empty()
        self._reset_bomb
        self._create_fleet()
        self.ship.center_ship()
        self.scoreboard.prep_score()
        # Pause
        pygame.time.delay(1000)
        
    def _check_bullet_collisions(self):
        """Check for collision with an alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            return True
            
    def _check_piercer_collisions(self):
        """Check for collision with an alien."""
        collisions = pygame.sprite.groupcollide(
            self.piercers, self.aliens, False, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            return True
        
    def _check_bomb_exploding(self):
        # Bomb doesn't earn points
        hit = False
        if self.settings.b_active:
            if self.settings.b_timer == 0:
                self.bomb.explode()
                bombs = pygame.sprite.Group()
                bombs.add(self.bomb)
                
                collisions = pygame.sprite.groupcollide(
                    bombs, self.aliens, False, True)
                if collisions:
                    for aliens in collisions.values():
                        self.stats.score += self.settings.alien_points * len(aliens)
                    hit = True
                bombs.empty()

                self.settings.b_active = False
                self.bomb.linger()
            else:
                self.settings.b_timer -= 1
    
        elif self.bomb.lingering:
            self.bomb.linger()
            if self.bomb.linger_timer <= 0:
                self._reset_bomb()
        return hit

    def _reset_bomb(self):
        self.bomb = Bomb(self)
        self.settings.b_timer = 240
        self.settings.b_active = False
    
    def _create_fleet(self):
        # Start by deleting any current aliens
        self.aliens.empty()
        """Create a row of aliens one width apart"""
        alien = Alien(self)        
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        x_padding = 3 * alien_width
        current_x = x_padding
        current_y = 10
        start_dir = 1
        while current_y < (self.settings.screen_height / 2):
            while current_x < (self.settings.screen_width - x_padding):
                self._create_alien(current_x, current_y, start_dir)
                current_x += 1.5*alien_width
            current_x = x_padding
            current_y += alien_height
            start_dir *= -1
            
    def _create_alien(self, x_pos, y_pos, direction):
        new_alien = Alien(self)
        new_alien.direction = direction
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos
        self.aliens.add(new_alien)
        
    def _update_aliens(self):
        # self._check_fleet_edge()
        self.aliens.update()
        
        # Look for ship/alien collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        self.path.open('a').write(f"You dead! {self.stats.ships_left} life(s) left!\n")
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()
            self._reset()
        else:
            pygame.mouse.set_visible(True)
            self.settings.initialize_dynamics()
            self.stats.reset_stats()
            self.game_active = False
        
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
        
    
    # def _check_fleet_edge(self):
    #     for alien in self.aliens.sprites():
    #         if alien.at_edge():
    #             self._change_fleet_direction()
    #             break
    
    # def _change_fleet_direction(self):
    #     for alien in self.aliens.sprites():
    #         alien.rect.y += self.settings.alien_downspeed
    #     self.settings.alien_right = not self.settings.alien_right

if __name__ == '__main__':
    game = Alienvasion()
    game.run_game()