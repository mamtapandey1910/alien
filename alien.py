import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image and it's rect attribute.
        self.image = pygame.image.load('alie.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)

