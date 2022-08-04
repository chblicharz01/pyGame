'''
Snake Game Authored by Sloan Kelly
written by Chris Blicharz
8-1-2022
'''

# importations
import pygame, os, sys
import random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)


class Position:
    def __init__(self, x, y):
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
        self.frame = 0

        bx = random.randint(1, 38)
        by = random.randint(1, 28)

        self.berry = Position(bx, by)
        self.blocks.append(Position(20, 15))
        self.blocks.append(Position(19, 15))
        self.direction = 0


def loseLife(gameData):
    pass


def positionBerry(gameData):
    pass


def loadMapFile(fileName):
    return None


def headHitBody(gameDate):
    return False


def headHitWall(map, gameData):
    return False


def drawData(surface, gamedata):
    pass


def drawGameOver(surface):
    pass


def drawWalls(surface, img, map):
    pass


def drawSnake(surface, img, gameData):
    pass


def updateGame(gameData, gameTime):
    pass


def loadImages():
    wall = pygame.image.load('wall.png')
    raspberry = pygame.image.load('berry.png')
    snake = pygame.image.load('snake.png')
    return {'wall':wall,'berry':raspberry,'snake':snake}


images = loadImages()
images['berry'].set_colorkey((255, 0, 255))

snakemap = loadMapFile('map.txt')
data = GameData()

quitGame = False
isPlaying = False

# main game logic
while not quitGame:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if isPlaying:
        x = random.randint(1, 38)
        y = random.randint(1, 28)

        rrect = images['berry'].get_rect()
        rrect.left = data.berry.x * 16
        rrect.top = data.berry.y * 16

        # Game update code here

        isPlaying = (data.lives > 0)
        if isPlaying:
            surface.fill((0, 0, 0))
            # drawing code will go here

    else:
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            isPlaying = True
            data = None
            data = GameData()
