import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('FIRST GUI')

COLOR1 = (255,255,255)
COLOR2 = (0, 0, 0)
COLOR3 = (255,255,0)
COLOR4 = (255,0, 255)
COLOR5 = (0, 255, 255)
COLOR6 = (255, 0, 0)

DISPLAYSURF.fill(COLOR1)
# pygame.draw.polygon(DISPLAYSURF, COLOR2, ((146, 0), (291,106), (236,277), (56,277), (0,106)))
# pygame.draw.line(DISPLAYSURF, COLOR3, (60,60), (120,60), 4)
# pygame.draw.line(DISPLAYSURF, COLOR3, (120,60), (60,120),20)
# pygame.draw.line(DISPLAYSURF, COLOR3, (60,120), (120,120), 10)
# pygame.draw.circle(DISPLAYSURF, COLOR4, (100,150), 50)
# pygame.draw.circle(DISPLAYSURF, COLOR5, (300,150), 50, 30)
# pygame.draw.ellipse(DISPLAYSURF, COLOR5, (100,100,200,100), 30)
pygame.draw.rect(DISPLAYSURF, COLOR2, (50,50,150,100))
pygame.draw.rect(DISPLAYSURF, COLOR3, (200,150,150,100), 20)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

