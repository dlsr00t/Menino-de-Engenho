import pygame
import os
from sys import exit
from pygame.locals import *

pygame.init()
largura = 1200
altura = 640
branco = 255, 255, 255
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
x = largura/2
y = altura/2
a = 0
b = 0
'''
while True:
    relogio.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
'''

pygame.display.set_caption('Jogo')
tela = pygame.display.set_mode((largura, altura))

pygame.init()

def sprite(sprite_name):
    global image_sprite
    image_sprite = [pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+ '1.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'2.png'))]


#def tela_de_start():
while True:
    relogio.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()