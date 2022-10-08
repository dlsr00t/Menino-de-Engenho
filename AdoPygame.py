import pygame
from pygame.locals import *
import random

c=0
d = 300
pygame.init()
x = random.randint(0, 1080)
y = random.randint(0,700)
tela = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('sla')

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()

    pygame.draw.rect(tela, (255,0,0), (10,10,40,50))
    #while c < 100:
    y = y+1

    pygame.display.update() 