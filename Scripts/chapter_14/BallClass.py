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

if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode((800,600))

    ball = Ball()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            ball.update(fpsClock)
            surface.fill((0,0,0))
            ball.draw(fpsClock, surface)

