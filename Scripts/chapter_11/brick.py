#authored by Sloan Kelly
#modified by Chris Blicharz

import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800,600))
pygame.display.set_caption('Bricks')

black = pygame.Color(0,0,0)

#controllable bat

bat = pygame.image.load('bat.png')
playerY = 540 #y coordinate is constant at 540

batRect = bat.get_rect()
mousex,mousey = (0, playerY)

#ball init
ball = pygame.image.load('ball.png')
ballRect = ball.get_rect()
ballStartY = 200
ballSpeed = 5
ballServed = False
bx, by = (24,ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx,by)

#brick init
brick = pygame.image.load('brick.png')
bricks = []
for y in range(5):
    brickY = (y * 24) + 100
    for x in range(10):
        brickX = (31 * x) + 245
        width = brick.get_width()
        height = brick.get_height()
        rect = Rect(brickX, brickY, width, height)
        bricks.append(rect)

while True:
    mainSurface.fill(black)

    #draw bat
    mainSurface.blit(bat, batRect)

    #draw ball
    mainSurface.blit(ball,ballRect)

    #draw brick
    for b in bricks:
        mainSurface.blit(brick,b)
    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex,mousey = event.pos
            if(mousex < 800-55):
                batRect.topleft = (mousex, playerY)
            else:
                batRect.topleft = (800 - 55, playerY)
        elif event.type == MOUSEBUTTONUP and not ballServed:
            ballServed = True

    #main game logic
    if ballServed:
        bx += sx
        by += sy
        ballRect.topleft = (bx ,by)

    #y movement
    if (by < 0):
        by = 0
        sy *= -1

    if (by >= 600 - 8):
        ballServed = False
        bx, by = (24, ballStartY)
        ballSpeed = 3
        sx, sy = (ballSpeed, ballSpeed)
        ballRect.topleft = (bx , by)

    #x movement
    if (bx <= 0 ):
        bx = 0
        sx *= -1

    if (bx >= 800 - 8):
        bx = 800 - 8
        sx *= -1

    #collision detection
    if ballRect.colliderect(batRect):
        by = playerY-8
        sy *= -1

    brick_hit_index = ballRect.collidelist(bricks)
    if brick_hit_index >= 0:
        hb = bricks[brick_hit_index]
        mx = bx + 4
        my = by + 4
        if mx > hb.x + hb.width or mx < hb.x:
            sx *= -1
        else:
            sy *= -1
        del (bricks[brick_hit_index])

    pygame.display.update()
    fpsClock.tick(30)

