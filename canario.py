import pygame
from pygame.locals import*
from sys import exit
from random import randint
import os

pygame.init()
a = 0 
b = 0
img_tio_juca = pygame.image.load(os.path.join('assets', 'tio_juca.png'))
tio_juca = pygame.transform.scale(img_tio_juca, (50, 81))
posicoesx = []
posicoesy = []
nnpode = [[a + 200, b + 200],[a + 300, b + 400],[a+400, b+50],[a+700, b+50],[a+900, b+350]]
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
donda = ''
donda_count = 0
pygame.display.set_caption('Jogo')
lista_de_colisao = [pygame.Rect(x_marrom, y_marrom, 32, 26)]
def sprite(sprite_name, largura=50, altura = 81):
    sprite_imagem = pygame.image.load(os.path.join('assets', sprite_name+'.png'))
    sprite_imagem = pygame.transform.scale(sprite_imagem, (largura, altura))
    tela.blit(sprite_imagem, (x, y))

numero = 0
while True:
    mensagem = f'Canários: {pontos}'
    texto_formatado = fonte.render(mensagem,False,(0, 0, 0))
    texto_rect = texto_formatado.get_rect()
    texto_rect.center = (largura/2, 100)
    relogio.tick(120)
    tela.fill((0,200,0))
    ret_azul = pygame.Rect(x, y, 50, 81)
    ret_marrom = pygame.Rect(x_marrom, y_marrom, 32, 26)

    tela.blit(canario, ret_marrom)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pontos = 0
                gambiarra3 = 0

    if pygame.key.get_pressed()[K_a]:
        #x=x-5


        if not ret_azul.colliderect(ret_marrom):
            x=x-5
            sprite("sprite_esquerda")
            ultimo = "sprite_esquerda"
            donda = 'a'
            


    elif pygame.key.get_pressed()[K_d]:
        #x=x+5

        if not ret_azul.colliderect(ret_marrom):
            x=x+5
            sprite("sprite_direita")
            ultimo = "sprite_direita"
            donda = 'd'
            #donda_count = 0

    elif pygame.key.get_pressed()[K_w]:
        #y=y-5
        if not ret_azul.colliderect(ret_marrom):
            y=y-5
            sprite("sprite_cima")
            ultimo = "sprite_cima"
            #if ret_azul.colliderect(ret_marrom):
            donda='w'


    elif pygame.key.get_pressed()[K_s]:
        #y=y+5
        if not ret_azul.colliderect(ret_marrom):
            y=y+5
            sprite("sprite_baixo")
            ultimo = "sprite_baixo"
            #if ret_azul.colliderect(ret_marrom):
            donda='s'


    #if ret_azul.colliderect(ret_marrom):
        #if gambiarra3 <= 0:
            #while sla<1:
    #            x_marrom=randint(40,1100)
    #            y_marrom=randint(50,550)
    #            pontos+=1
    #            sla +=1



     
    if ret_azul.colliderect(ret_marrom) and donda == 'a':
        x=x+5
    elif ret_azul.colliderect(ret_marrom) and donda == 'd':
        x=x-5
    elif ret_azul.colliderect(ret_marrom) and donda == 'w':
        y=y+5
    elif ret_azul.colliderect(ret_marrom) and donda == 's':
        y=y-5

    
    
    if ret_azul.colliderect(ret_marrom):
        print("so pra ver")
        #x_marrom=randint(40,1100)
        #y_marrom=randint(50,550)
        x_marrom = randint(40, 1100)
        pontos+=1
        sla+=1
        for c in nnpode:
            #print(c[0])
            posicoesx.append(c[0])

        #print(posicoesx)
        if x_marrom in posicoesx:
            print("valor igual")
            posicoesx = []
        #else:
        #    print("passou: ",x_marrom)
            


        y_marrom = randint(50, 550)
        for c in nnpode:
            posicoesy.append(c[1])

        #print(posicoesy)
        if y_marrom in posicoesy:
            print("valor igual")
            posicoesy = []
        #else:
            #print("passou(y): ",y_marrom)
    
    if ret_azul.collidelist(lista_de_colisao)>=0:
        print("colidiu: ", numero)
        numero+=1

    if pontos == 0:
        x_marrom = 900 
        y_marrom = 200
        
    if pontos >= 3:
        
        x_marrom = 900 
        y_marrom = 200
        texto_formatado = fonte.render(nada, False, (255,255,255))

    tela.blit(texto_formatado, texto_rect)
    
    sprite(ultimo)
    #tst = pygame.sprite.Group()
    #tst.add(tio_juca)
    #if donda != '':
        #print("donda:",donda)
        #exit()
        #break
    pygame.display.flip()


print("donda fora do while true: ", donda)
