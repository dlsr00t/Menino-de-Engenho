import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

largura = 640
altura = 480
branco = 255, 255, 255


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

sprite_sheet = pygame.image.load(os.path.join('assets', 'spritesheet.png')).convert_alpha()

class Personagem(pygame.sprite.Sprite):
    j = 0
    i=0
    def __init__(self, i=0, j=0):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_perso = []
        for i in range(4):
            img = sprite_sheet.subsurface((i * 11, j * 18), (11, 18))
            img = pygame.transform.scale(img, (50, 81))
            self.imagens_perso.append(img)

        


        self.index_lista = 0
        self.image = self.imagens_perso[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self):
        if self.index_lista > 3:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_perso[int(self.index_lista)]

todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key==K_a:
                #j += 3
                todas_as_sprites = pygame.sprite.Group()
                esquerda = Personagem(j=3)
                todas_as_sprites.add(esquerda)            
                
            

            if event.key == K_d:
                #j += 2
                direita = Personagem(j=2)
                todas_as_sprites = pygame.sprite.Group()
                todas_as_sprites.add(direita)            


            if event.key == K_w:
                #j += 1
                cima = Personagem(j=1)
                todas_as_sprites = pygame.sprite.Group()
                todas_as_sprites.add(cima)            


            if event.key == K_s:
                #j = j
                baixo = Personagem()
                todas_as_sprites = pygame.sprite.Group()
                todas_as_sprites.add(baixo)                            


    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()

'''
        if pygame.key.get_pressed()[K_a]:
            j = j + 3
            personagem = Personagem()
            todas_as_sprites.add(personagem)
            


        if pygame.key.get_pressed()[K_d]:
            j = j + 2
            personagem = Personagem()
            todas_as_sprites.add(personagem)
            

        if pygame.key.get_pressed()[K_w]:
            j = j + 1
            personagem = Personagem()
            todas_as_sprites.add(personagem)

        if pygame.key.get_pressed()[K_s]:
            j = j
            personagem = Personagem()
            todas_as_sprites.add(personagem)

'''

    #todas_as_sprites.draw(tela)
    #todas_as_sprites.update()

    #pygame.display.flip()