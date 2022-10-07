import pygame
from pygame.locals import *
from sys import exit
import os


pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2
branco = 255, 255, 255
sprite_frente_imagem = pygame.image.load(os.path.join('assets', 'sprite_frente.png'))
sprite_frente = pygame.transform.scale(sprite_frente_imagem, (50, 81))

sprite_cima_imagem = pygame.image.load(os.path.join('assets', 'sprite_cima.png'))
sprite_cima_imagem = pygame.transform.scale(sprite_cima_imagem, (50, 81))

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
tela.fill(branco)
tela.blit(sprite_frente, (x, y))

while True:
    relogio.tick(60)
    #tela.fill(branco)
    #tela.blit(sprite_frente, (x, y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''
    if pygame.key.get_pressed()[K_a]:
        x = x - 5
        sprite_frente_imagem = pygame.image.load(os.path.join('assets', 'sprite_cima.png'))
        sprite_frente_imagem = pygame.transform.scale(sprite_frente_imagem, (50, 81))
        tela.fill(branco)
        tela.blit(sprite_frente_imagem, (x, y))
    if pygame.key.get_pressed()[K_d]:
        x = x + 5
        sprite_frente_imagem = pygame.image.load(os.path.join('assets', 'sprite_cima.png'))
        sprite_frente_imagem = pygame.transform.scale(sprite_frente_imagem, (50, 81))
        tela.fill(branco)
        tela.blit(sprite_frente_imagem, (x, y))
    if pygame.key.get_pressed()[K_w]:
        y = y - 5
        sprite_frente_imagem = pygame.image.load(os.path.join('assets', 'sprite_cima.png'))
        sprite_frente_imagem = pygame.transform.scale(sprite_frente_imagem, (50, 81))
        tela.fill(branco)
        tela.blit(sprite_frente_imagem, (x, y))
    if pygame.key.get_pressed()[K_s]:
        y = y + 5
        sprite_frente_imagem = pygame.image.load(os.path.join('assets', 'sprite_frente.png'))
        sprite_frente_imagem = pygame.transform.scale(sprite_frente_imagem, (50, 81))
        tela.fill(branco)
        tela.blit(sprite_frente_imagem, (x, y))
    pygame.display.update()