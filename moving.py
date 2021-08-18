

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
rightImg = pygame.transform.scale(img, (WIDTH, HEIGHT))
leftImg = pygame.transform.flip(rightImg, True, False)

imgRect = pygame.Rect((0,0,WIDTH,HEIGHT))


moveUp=False
moveDown=False
moveLeft=False
moveRight=False
sideRight = True

while True:
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                moveDown = False
                moveUp = True
            elif event.key in (K_DOWN, K_s):
                moveUp = False
                moveDown = True
            elif event.key in (K_LEFT, K_a):
                moveRight = False
                moveLeft = True
                sideRight = False
            elif event.key in (K_RIGHT, K_d):
                moveLeft = False
                moveRight = True
                sideRight = True
        elif event.type == KEYUP:
            # stop moving the player's squirrel
            if event.key in (K_LEFT, K_a):
                moveLeft = False
            elif event.key in (K_RIGHT, K_d):
                moveRight = False
            elif event.key in (K_UP, K_w):
                moveUp = False
            elif event.key in (K_DOWN, K_s):
                moveDown = False

    if moveUp :
        imgRect.y -= 3
    if moveDown :
        imgRect.y += 3
    if moveRight :
        imgRect.x += 3
    if moveLeft:
        imgRect.x -= 3

    if sideRight:
        DISPLAYSURF.blit(rightImg,imgRect)
    else:
        DISPLAYSURF.blit(leftImg,imgRect)

    pygame.display.update()
    fpsClock.tick(FPS)