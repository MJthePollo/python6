import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('FIRST GUI')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
SKYBLUE = (50,255,255)
BLUE = (0,0,255)

DISPLAYSURF.fill(BLUE)
pygame.draw.polygon(DISPLAYSURF, RED, ((50,120),(200,60),(350,120)))
pygame.draw.rect(DISPLAYSURF, WHITE, (100,120,200,120))
pygame.draw.rect(DISPLAYSURF, SKYBLUE, (170,150,60,40))
pygame.draw.rect(DISPLAYSURF, GREEN, (0,240,400,60))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

