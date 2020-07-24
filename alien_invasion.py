import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        # to initiate the pygame, and create game resource
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((1200, 800))
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height == self.screen.get_rect().height
        self.caption = pygame.display.set_caption("Alien Invasion")
        # setting the background color

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # start the main loop for the game
        while True:
            self._check_event()
            self.ship.update()
            self.bullets.update()
            self.update_screen()

    def _check_event(self):
        # response to the keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._key_down(event)

            elif event.type == pygame.KEYUP:
                self._key_up(event)


    def _key_down(self, event):
        # responds to the keypresses..
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _key_up(self, event):
        # responds to the key release..
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ create a new bullet and add it bullets group"""
        new_bullet= Bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        """To update the images on the screen and flip the new screen"""
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
