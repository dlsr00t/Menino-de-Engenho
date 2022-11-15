import pygame
from pygame.locals import*
from sys import exit
from random import randint
import os

pygame.init()

fonte=pygame.font.SysFont('arial',40,True,True)
x_marrom=randint(40,1100)
y_marrom=randint(50,550)
largura = 1200
altura = 640
x=largura/2
y=altura/2
relogio=pygame.time.Clock()
tela=pygame.display.set_mode((largura, altura))
pontos=0
sla = 0
#mensagem=f'pontos:{pontos}'
#texto_formatado=fonte.render(mensagem,False,(255,255,255))
musica = pygame.mixer.music.load(os.path.join('assets', "mega"+'.mp3'))
pygame.mixer.music.play(-1)

pygame.display.set_caption('Jogo')
while True:
    mensagem=f'pontos:{pontos}'
    texto_formatado=fonte.render(mensagem,False,(255,255,255))
    relogio.tick(120)
    tela.fill((0,200,0))
    ret_azul=pygame.draw.rect(tela,(0,0,255),(x,y,40,50))
    ret_marrom=pygame.draw.rect(tela,(150,75,0),(x_marrom,y_marrom,150,200))
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
        x=x-7
    if pygame.key.get_pressed()[K_d]:
        x=x+7
    if pygame.key.get_pressed()[K_w]:
        y=y-7
    if pygame.key.get_pressed()[K_s]:
        y=y+7
    if ret_azul.colliderect(ret_marrom):
        while sla<1:
            x_marrom=randint(40,1100)
            y_marrom=randint(50,550)
            pontos+=1
            sla +=1

    if not ret_azul.colliderect(ret_marrom):
        sla = 0

    if ret_azul.colliderect(ret_marrom):
        while sla<1:
            print('colidiu') 
            sla += 1

    if not ret_azul.colliderect(ret_marrom):
        sla = 0

    tela.blit(texto_formatado,(900,160))

    pygame.display.update()
