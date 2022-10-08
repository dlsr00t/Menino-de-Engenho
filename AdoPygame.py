import pygame
from pygame.locals import *

pygame.init()
musica = pygame.mixer.music.load("megalovania.mp3")
pygame.mixer.music.play(-1)

while True:
    print("hi")
'''
tela = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Joguin")
x = 0
y = 0
relogio = pygame.time.Clock()
 
while True:
    relogio.tick(120)
    tela.fill((255,255,255))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()

    pygame.draw.rect(tela, (255,0,0), (x,y, 50,50))
    y = y+1
    x = x+1
    if y > 720:
        y = 0
    if x > 1080:
        x = 0

    pygame.display.update()'''