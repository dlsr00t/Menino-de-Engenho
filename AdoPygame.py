import pygame
from pygame.locals import *



tela = pygame.display.set_mode((720, 480))
pygame.display.set_caption("tst")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
    pygame.display.update()