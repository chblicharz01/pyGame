"""
Space Explorer Authored by Chris Blicharz
Started on 8-11-2022
Ongoing Project
"""

#importations
import pygame, os, sys
import random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640,480))
font = pygame.font.Font(None, 32)

def drawEntry(surface):
	text1 = font.render("Space Explorer!", 1, (255,255,255))
	text2 = font.render("Click Anywhere to Start...", 1, (255,255,255))
	cx = surface.get_width() /2
	cy = surface.get_height() /2
	text_pos_1 = text1.get_rect(centerx = cx, top = cy-48)
	text_pos_2 = text2.get_rect(centerx = cx, top = cy)

	surface.blit(text1, text_pos_1)
	surface.blit(text2, text_pos_2)


quitGame = False
isPlaying = False
while not quitGame:
	if isPlaying:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	else:

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		drawEntry(surface)
		bg = pygame.image.load("bg.png")
		
		surface.blit(bg, (320,240))
	pygame.display.update()
	fpsClock.tick(30)
