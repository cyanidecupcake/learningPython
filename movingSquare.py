#!/usr/local/bin/python

import pygame
from pygame.locals import *
import sys

pygame.init() ##initalizes pygame

clock = pygame.time.Clock() ##refreshes the screen
fps = 15

##create world
canvas_width = 960
canvas_height = 720
canvas = pygame.display.set_mode([canvas_width, canvas_height])
pygame.display.set_caption('Moving Square') ##sets window title


##create variables for world 
black = (26, 26, 26)


##create classes
class hero(pygame.Rect): ##create class
	def __init__(self,rx,ry):
		pygame.draw.rect(canvas, (100, 200, 250), Rect((rx, ry), (40,40)))  ##surface, colour, location, size


##player sprite below    
rx = 50 ##sets sprite origin x
ry = 50 ##sets sprite origin y
player = hero(rx, ry)
	

##Loop

main = True
while main == True:	
	pygame.display.flip() ##redraws screen
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit();
					
		##Movement 
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				rx = rx-10
				canvas.fill(black)  ##refreshes the screen to prevent square trail
				player = hero(rx, ry)
			if event.key == K_RIGHT:
				rx = rx+10
				canvas.fill(black)
				player = hero(rx, ry)
			if event.key == K_UP:
				ry = ry-10
				canvas.fill(black)
				player = hero(rx, ry)
			if event.key == K_DOWN:
				ry = ry+10
				canvas.fill(black)
				player = hero(rx, ry)

				
				




	

				
