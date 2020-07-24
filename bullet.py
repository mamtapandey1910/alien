import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage bullets from the ship"""
    def __init__(self,ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = ai_game.setting.bullet_color

        # create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0,self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        # update the deciml posiion of the bullet.
        self.y -= self.setting.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

