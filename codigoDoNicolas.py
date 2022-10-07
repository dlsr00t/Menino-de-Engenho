from time import time
import pygame
from pygame.locals import*
from sys import exit
from random import randint
import time

pygame.init()

sla = 0
x_marrom=randint(40,600)
y_marrom=randint(50,430)
largura = 1200
altura = 640
x=largura/2
y=altura/2
relogio=pygame.time.Clock()
tela=pygame.display.set_mode((largura, altura))



pygame.display.set_caption('Jogo')
while True:
    
    relogio.tick(60)
    tela.fill((0,200,0))
    ret_azul=pygame.draw.rect(tela,(0,0,255),(x,y,40,50))
    ret_marrom=pygame.draw.rect(tela,(150,75,0),(430,300,150,200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key==K_a:
                x=x-20
            if event.key==K_d:
                x=x+20
            if event.key==K_w:
                y=y-20
            if event.key==K_s:
                y=y+20 '''
    if pygame.key.get_pressed()[K_a]:
        x=x-10
    if pygame.key.get_pressed()[K_d]:
        x=x+10
    if pygame.key.get_pressed()[K_w]:
        y=y-10
    if pygame.key.get_pressed()[K_s]:
        y=y+10

    
    if ret_azul.colliderect(ret_marrom):
        while sla<1:
            print('colidiu') 
            sla += 1
        
    if not ret_azul.colliderect(ret_marrom):
        sla = 0


    pygame.display.update()