import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

largura = 640
altura = 480
branco = 255, 255, 255
x = largura/2
y = altura/2

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
            global img
            img = sprite_sheet.subsurface((i * 11, j * 18), (11, 18))
            img = pygame.transform.scale(img, (50, 81))
            self.imagens_perso.append(img)

        


        self.index_lista = 0
        self.image = self.imagens_perso[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

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

       # if event.type == KEYDOWN:
        if pygame.key.get_pressed()[K_a]:
            #j += 3
            x -= 2.5
            todas_as_sprites = pygame.sprite.Group()
            esquerda = Personagem(j=3)
            todas_as_sprites.add(esquerda)  
            tela.fill(branco)
            tela.blit(img, (x,y))    
            todas_as_sprites.remove(esquerda)      
                
            

        if pygame.key.get_pressed()[K_d]:
            #j += 2
            x+=2.5
            direita = Personagem(j=2)
            todas_as_sprites = pygame.sprite.Group()
            todas_as_sprites.add(direita)   
            tela.blit(img, (x,y))         
            todas_as_sprites.remove(direita)


        if pygame.key.get_pressed()[K_w]:
            #j += 1
            y-=4
            cima = Personagem(j=1)
            todas_as_sprites = pygame.sprite.Group()
            todas_as_sprites.add(cima)  
            tela.blit(img, (x,y))       
            todas_as_sprites.remove(cima)   


        if pygame.key.get_pressed()[K_s]:
            #j = j
            
            y+=4
            #baixo = Personagem()
            #todas_as_sprites = pygame.sprite.Group()
            #todas_as_sprites.add(baixo)  
            tela.blit(img, (x,y))  
            #todas_as_sprites.remove(baixo)
            
            
                       


    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    

    pygame.display.update()

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