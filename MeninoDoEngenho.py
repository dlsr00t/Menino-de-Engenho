from glob import glob
import pygame
from pygame.locals import *
from sys import exit
import os
import time
from variaveis import *

pygame.display.set_caption('Menino do Engenho')

rodando = False
valor_continuar = 0
contador = 0


def sprite(sprite_name):
    global image_sprite
    image_sprite = [pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+ '1.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'2.png'))]



def tela_de_start():      
    global rodando
    global valor_continuar
    global continuar
    fonte_start = pygame.font.SysFont('arial', 30, True, True)
    start = 'Pressione qualquer tecla para continuar'
    continuar = [fonte_start.render(start, False, (branco)),
                 fonte_start.render(start, False, (preto))] 
    if valor_continuar >= len(continuar):
        valor_continuar = 0
    pressione = continuar[int(valor_continuar)]
    continuar_rect = pressione.get_rect()
    continuar_rect.midtop = (largura/2, 500)
    tela.blit(pressione, continuar_rect)
    titulo = pygame.image.load(os.path.join('assets', 'logo.png'))
    logo = pygame.transform.scale(titulo, (520, 250))
    logo_rect = logo.get_rect()
    logo_rect.midtop = (largura/2, 100)
    tela.blit(logo, logo_rect)



def instrucoes():
    instrucoes = pygame.Rect(largura/2, altura/2, 500, 140)
    instrucoes.midtop = (largura/2, 220)
    pygame.draw.rect(tela, branco, instrucoes)
    mensagem = 'Pressione W, A, S e D para andar'
    fonte = pygame.font.SysFont('arial', 30, True, True)
    controles = fonte.render(mensagem, False, (0, 0, 0))
    controles_rect = controles.get_rect()
    controles_rect.center = (largura/2, 240)
    tela.blit(controles, controles_rect)
    mensagem2 = 'Pressione E para interagir'
    controles2 = fonte.render(mensagem2, False, (0, 0, 0))
    controles_rect2 = controles2.get_rect()
    controles_rect2.center = (largura/2, 340)
    tela.blit(controles2, controles_rect2)



def dialogo(ret1 = "ret_um", ret2 = "ret_dois", ret2_cord_a=200, ret2_cord_b = 281):
    ret1 = pygame.Rect(x, y, 50, 81)
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
        texto_count = 0     #hookando
        texto = False       #hookando



def hook_para_dialogo():
    global texto
    global texto_count
    if event.type == KEYDOWN:
        '''
        ret_um = pygame.Rect(x, y, 50, 81)
        ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)
        if ret_um.colliderect(ret_dois):
            tela.blit(nome_formatado, (a + 175, b + 150))
        '''
        global contador
        contador +=1
        if event.key==K_e:   
            ret_um = pygame.Rect(x, y, 50, 81)
            ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)             
            if ret_um.colliderect(ret_dois) and texto_count <= len(mensagem):
                #tela.blit(texto_formatado, (a + 175, b + 150))
                texto = True        #hook
                texto_count += 1    #hook



def esta_em_movimento():
    global valor
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
            #movimentando = False
            valor = 0
            return False



def mostrar(estado, fundo = "preto"):
    tela.fill(fundo)
    relogio.tick(30)
    estado()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            global rodando
            rodando = True
    
    global valor_continuar
    valor_continuar += 0.075
    pygame.display.flip()



while (rodando == False):
    mostrar(tela_de_start)


while (rodando == True):
    relogio.tick(30)
    tela.fill(branco)
    tela.blit(background, (a, b))
    tela.blit(npc, (a + 200, b + 200))
    sprite(ultimo)    
    dialogo()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        movimentando = esta_em_movimento()         
        hook_para_dialogo()
        

    if pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_d]:
        ultimo = ultimo

    elif pygame.key.get_pressed()[K_a]:
        if x > a:
            x -= 4
            movimentando = True
            sprite("sprite_esquerda")
            ultimo = "sprite_esquerda"
            a += 4

    elif pygame.key.get_pressed()[K_d]:
        if x + 50 < a + 1200:
            x += 4
            movimentando = True
            sprite("sprite_direita")
            ultimo = "sprite_direita"
            a -= 4



    if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_s]:
        ultimo = ultimo

    elif pygame.key.get_pressed()[K_w]:
        if y > b:
            y -= 4
            movimentando = True
            sprite("sprite_cima")
            ultimo = "sprite_cima"
            b += 4

    elif pygame.key.get_pressed()[K_s]:
        if y + 81 < b + 640:
            y += 4
            movimentando = True
            sprite("sprite_baixo")
            ultimo = "sprite_baixo"
            b -= 4



    if movimentando == True:
        valor += 0.25
    else:
        valor = 0

    if valor >= len(image_sprite):
        valor = 0

    imagem = image_sprite[int(valor)]
    imagem = pygame.transform.scale(imagem, (50, 81))

    tela.blit(imagem, (x, y))
    
    if contador <= 0:
        instrucoes()
        
    '''
    ret_um = pygame.Rect(x, y, 50, 81)
    ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)
    if ret_um.colliderect(ret_dois):     
        tela.blit(nome_formatado, (a + 175, b + 150))
    '''
    
    #tela.blit(nome_formatado, (a + 175, b + 150))
    pygame.display.flip()