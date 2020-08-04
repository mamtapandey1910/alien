import pygame
from settings import Settings

class Ship:
    def __init__(self,ai_game):
        """inialize the ship and it's starting point"""
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()


        #load the image and get it's rect
        self.image = pygame.image.load('rocket.bmp')
        self.image = pygame.transform.scale(self.image,(150,100))
        self.rect= self.image.get_rect()

        #start the ship at the bottom centre of the screen
        self.rect.midbottom= self.screen_rect.midbottom

        #store the value of ship'shorizontal position
        self.x= float(self.rect.x)
        #movements flags
        self.moving_right= False
        self.moving_left = False

    def update(self):
        """update the ship position on the basis of movement flag"""
        #update the ship's x value not the rect
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.setting.ship_speed

        #update the rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """ center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)