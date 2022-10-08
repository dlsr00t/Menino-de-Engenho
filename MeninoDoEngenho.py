import pygame
from pygame.locals import *
from sys import exit
import os
import time

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2
branco = 255, 255, 255

def sprite(sprite_name, largura=50, altura = 81):
    sprite_imagem = pygame.image.load(os.path.join('assets', sprite_name+'.png'))
    sprite_imagem = pygame.transform.scale(sprite_imagem, (largura, altura))
    tela.fill(branco)
    tela.blit(sprite_imagem, (x, y))


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
relogio.tick(60)
sprite("sprite_frente")

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 2.5
        sprite("sprite_esquerda", largura=26)
        
    if pygame.key.get_pressed()[K_d]:
        x = x + 2.5
        sprite("sprite_direita", largura=26)
 
    if pygame.key.get_pressed()[K_w]:
        y = y - 4
        sprite("sprite_cima")

    if pygame.key.get_pressed()[K_s]:
        y = y + 4
        sprite("sprite_frente")
    
    if pygame.key.get_pressed()[K_SPACE]:
        pass
        

    pygame.display.update()
