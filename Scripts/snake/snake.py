'''
Snake Game Authored by Sloan Kelly
written by Chris Blicharz
8-1-2022
'''

#importations
import pygame, os, sys
import random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640,480))
font = pygame.font.Font(None, 32)

class Position:
    def __init__(self, x,y):
        self.x = x
        self.y = y
class GameData:
    def __init__(self):
        self.lives = 3
        self.isDead = False
        self.blocks = []
        self.tick = 250
        self.speed = 250
        self.level = 1
        self.berrycount = 0
        self.segments = 1
        self.frame - 0

        bx = random.randint(1, 38)
        by = random.randint(1 , 28)

        self.berry = Position(bx, by)
        self.blocks.append(Position(20,15))
        self.blocks.append(Position(19,15))


