from glob import glob
import pygame
from pygame.locals import *
from sys import exit
import os
import time


largura = 1200
altura = 640
branco = 255, 255, 255
ultimo = "sprite_baixo"
mapa = pygame.image.load(os.path.join('assets', 'mapa.png'))
background = pygame.transform.scale(mapa, (1200, 640))
personagem = pygame.image.load(os.path.join('assets', 'npc.png'))
npc = pygame.transform.scale(personagem, (50, 81))
pygame.font.init()
fonte = pygame.font.SysFont('arial', 20, True, True)
mensagem = ['Salve','tchau', '']
texto_formatado = fonte.render(mensagem[0], False, (255, 255, 255))
nome = "joao"
nome_formatado = fonte.render(nome, False, (0,0,0))
nada = ''
nada_formatado = fonte.render(nome,False, (0,0,0))
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
valor = 0
movimentando = False
velocity = 12
x = largura/2
y = altura/2
a = 0
b = 0
#ret_um = pygame.Rect(x, y, 50, 81)
#ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)
texto = False
texto_count = 0
pygame.display.set_caption('Jogo')


def sprite(sprite_name):
    global image_sprite
    image_sprite = [pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+ '1.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'2.png'))]


while True:
    relogio.tick(30)
    tela.fill(branco)
    tela.blit(background, (a, b))
    tela.blit(npc, (a + 200, b + 200))
    sprite(ultimo)
    

    

    def dialogo(ret1 = "ret_um", ret2 = "ret_dois", ret2_cord_a=200, ret2_cord_b = 281):
        ret1 = pygame.Rect(x, y, 50, 81)
        #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
        ret2 = pygame.Rect(a+ret2_cord_a, b+ret2_cord_b, 50, 81)
        global texto
        global texto_count
        if ret1.colliderect(ret2):
            if not texto:
                formatacao = fonte.render(nome, False, (255,255,255))
                tela.blit(formatacao, (a + 175, b + 150))
            if texto == True and texto_count <= len(mensagem):
                formatacao = fonte.render(mensagem[texto_count-1], False, (0,0,0))
                tela.blit(formatacao, (a+175, b+150))
    
        if not ret1.colliderect(ret2) or texto_count > len(mensagem):
            texto_count = 0
            texto = False
    
    dialogo()
   
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        def is_moving():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                    #movimentando = False
                    valor = 0
                    return False
        
        movimentando = is_moving()
        
        def hook():
            global texto
            global texto_count
            if event.type == KEYDOWN:
                '''
                ret_um = pygame.Rect(x, y, 50, 81)
                ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)

                if ret_um.colliderect(ret_dois):
                    tela.blit(nome_formatado, (a + 175, b + 150))
                '''

                if event.key==K_e:   
                    ret_um = pygame.Rect(x, y, 50, 81)
                    ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)             
                    if ret_um.colliderect(ret_dois) and texto_count <= len(mensagem):
                        #tela.blit(texto_formatado, (a + 175, b + 150))
                        texto = True
                        texto_count += 1
                    
        hook()
        

    if pygame.key.get_pressed()[K_a]:
        if x > a:
            x -= 4
            movimentando = True
            sprite("sprite_esquerda")
            ultimo = "sprite_esquerda"
            a += 4

    if pygame.key.get_pressed()[K_d]:
        if x + 50 < a + 1200:
            x += 4
            movimentando = True
            sprite("sprite_direita")
            ultimo = "sprite_direita"
            a -= 4

    if pygame.key.get_pressed()[K_w]:
        if y > b:
            y -= 4
            movimentando = True
            sprite("sprite_cima")
            ultimo = "sprite_cima"
            b += 4

    if pygame.key.get_pressed()[K_s]:
        if y + 81 < b + 640:
            y += 4
            movimentando = True
            sprite("sprite_baixo")
            ultimo = "sprite_baixo"
            b -= 4


    if movimentando == True:
        valor += 0.25


    if valor >= len(image_sprite):
        valor = 0

    imagem = image_sprite[int(valor)]
    imagem = pygame.transform.scale(imagem, (50, 81))

    tela.blit(imagem, (x, y))


    '''
    ret_um = pygame.Rect(x, y, 50, 81)
    ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)

    if ret_um.colliderect(ret_dois):     
        tela.blit(nome_formatado, (a + 175, b + 150))
    '''
    
    #tela.blit(nome_formatado, (a + 175, b + 150))
    pygame.display.flip()

