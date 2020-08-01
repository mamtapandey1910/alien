import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        # start the main loop for the game
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self.update_screen()

    def _update_bullets(self):
        """ update the position of the bullets and get rid of old bullets"""
        # update bullet positios
        self.bullets.update()

        # to get rid of the bullets that disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


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
        if len(self.bullets) < self.setting.bullets_allowed:
            new_bullet= Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """ Create the fleet of aliens"""
        # create an alien and find the number of aliens in a row
        # Spacing btween alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of row of aliens that fit into the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.setting.screen_height)- (2* alien_height) - ship_height
        number_rows = (available_space_y)// (2* alien_height)

        # create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2* alien_height* row_number)
        self.aliens.add(alien)

    def update_screen(self):
        """To update the images on the screen and flip the new screen"""
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
