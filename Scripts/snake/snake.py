"""
Snake Game Authored by Sloan Kelly
written by Chris Blicharz
8-1-2022
"""

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
    f = open(fileName, 'r')
    content = f.readlines()
    f.close()
    return content


def headHitBody(gameDate):
    return False


def headHitWall(map, gameData):
    return False


def drawData(surface, gamedata):
    text = "Lives = {0}, Level = {1}"
    info = text.format(gamedata.lives, gamedata.level)
    text = font.render(info, 0, (255,255,255))
    textpos = text.get_rect(centerx=surface.get_width()/2, top= 32)
    surface.blit(text, textpos)
    pass


def drawGameOver(surface):
    text1 = font.render("Game Over", 1, (255, 255, 255))
    text2 = font.render("Hit Space to Play Again...", 1, (255, 255, 255))
    cx = surface.get_width() / 2
    cy = surface.get_height() / 2
    textpos1 = text1.get_rect(centerx=cx, top=cy - 48)
    textpos2 = text2.get_rect(centerx=cx, top=cy)

    surface.blit(text1, textpos1)
    surface.blit(text2, textpos2)



def drawWalls(surface, img, map):
    row = 0
    for line in map:
        col = 0
        for char in line:
            if char == '1':
                imgRect = img.get_rect()
                imgRect.left = col * 16
                imgRect.top = row * 16
                surface.blit(img, imgRect)
            col += 1
        row += 1


def drawSnake(surface, img, gameData):
    pass


def updateGame(gameData, gameTime):
    pass


def loadImages():
    wall = pygame.image.load('wall.png')
    raspberry = pygame.image.load('berry.png')
    snake = pygame.image.load('snake.png')
    return {'wall': wall, 'berry': raspberry, 'snake': snake}


images = loadImages()
images['berry'].set_colorkey((255, 0, 255))

snakemap = loadMapFile('map.txt')
data = GameData()

quitGame = False
isPlaying = False

# main game logic
while not quitGame:

    if isPlaying:
        x = random.randint(1, 38)
        y = random.randint(1, 28)

        rrect = images['berry'].get_rect()
        rrect.left = data.berry.x * 16
        rrect.top = data.berry.y * 16

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Game update code here

        isPlaying = (data.lives > 0)
        if isPlaying:
            surface.fill((0, 0, 0))
            # drawing code will go here
            drawWalls(surface, images['wall'], snakemap)
            surface.blit(images['berry'], rrect)
            drawSnake(surface, images['snake'], data)
            drawData(surface, data)

    else:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if keys[K_SPACE]:
            isPlaying = True
            data = None
            data = GameData()
        drawGameOver(surface)
    pygame.display.update()
    fpsClock.tick(30)
