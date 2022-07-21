import pygame, os, sys
from pygame.locals import *

class Ball:
    x = 0
    y = 200
    speed = (4,4)
    img = pygame.image.load('ball.png')

    def update(self, gameTime):
        pass
    def hasHitBrick(self,bricks):
        return False
    def hasHitBat(self, bat):
        return False
    def draw(self, gameTime, surface):
        surface.blit(self.img, (self.x, self.y))