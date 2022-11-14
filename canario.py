import pygame
from pygame.locals import*
from sys import exit
from random import randint
import os

pygame.init()

fonte=pygame.font.SysFont('arial',40,True,True)
x_marrom = 900
y_marrom = 200
largura = 1200
altura = 640
x=largura/2
y=altura/2
relogio=pygame.time.Clock()
tela=pygame.display.set_mode((largura, altura))
pontos=0
sla = 0
gambiarra3 = 0
nada = ' '
canario = pygame.image.load(os.path.join('assets', 'canario.png'))
canario = pygame.transform.scale(canario, (32, 32))
ultimo = "sprite_baixo"

pygame.display.set_caption('Jogo')

def sprite(sprite_name, largura=50, altura = 81):
    sprite_imagem = pygame.image.load(os.path.join('assets', sprite_name+'.png'))
    sprite_imagem = pygame.transform.scale(sprite_imagem, (largura, altura))
    tela.blit(sprite_imagem, (x, y))

while True:
    mensagem = f'Canários: {pontos}'
    texto_formatado = fonte.render(mensagem,False,(0, 0, 0))
    texto_rect = texto_formatado.get_rect()
    texto_rect.center = (largura/2, 100)
    relogio.tick(120)
    tela.fill((0,200,0))
    ret_azul = pygame.Rect(x, y, 50, 81)
    ret_marrom = pygame.Rect(x_marrom, y_marrom, 32, 32)
    tela.blit(canario, ret_marrom)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_e:
                pontos = 0
                gambiarra3 = 0

    if pygame.key.get_pressed()[K_a]:
        x=x-5
        sprite("sprite_esquerda")
        ultimo = "sprite_esquerda"

    if pygame.key.get_pressed()[K_d]:
        x=x+5
        sprite("sprite_direita")
        ultimo = "sprite_direita"

    if pygame.key.get_pressed()[K_w]:
        y=y-5
        sprite("sprite_cima")
        ultimo = "sprite_cima"

    if pygame.key.get_pressed()[K_s]:
        y=y+5
        sprite("sprite_baixo")
        ultimo = "sprite_baixo"


    if ret_azul.colliderect(ret_marrom):
        if gambiarra3 <= 0:
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

    if pontos == 0:
        x_marrom = 900 
        y_marrom = 200
        
    if pontos >= 3:
        gambiarra3 += 1
        x_marrom = 900 
        y_marrom = 200
        texto_formatado = fonte.render(nada, False, (255,255,255))

    tela.blit(texto_formatado, texto_rect)

    sprite(ultimo)

    pygame.display.flip()