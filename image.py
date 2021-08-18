

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
WIDTH=100
HEIGHT=100

img = pygame.image.load('big_tortoise.png')
img = pygame.transform.scale(img, (WIDTH, HEIGHT))
imgRect = pygame.Rect((0,0,WIDTH,HEIGHT))

while True:
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(img,imgRect)

    pygame.display.update()
    fpsClock.tick(FPS)



    