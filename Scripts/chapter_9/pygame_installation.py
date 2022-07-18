import pygame, os, sys
from pygame.locals import *

#initializing pygame
pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((800, 600))

background = pygame.Color(28, 20, 44)


while True:
    surface.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(30)
