from glob import glob
import pygame
from pygame.locals import *
from sys import exit
import os
import time
from variaveis import *
from pygame import mixer

pygame.display.set_caption('Menino do Engenho')

mixer.init()

rodando = False
valor_continuar = 0
contador = 0
valor_cutscene = 0
gambiarra = 0
gambiarra2 = 0
c = 1300

def sprite(sprite_name):
    global image_sprite
    image_sprite = [pygame.image.load(os.path.join('assets', sprite_name+'_4anos.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+ '1_4anos.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'_4anos.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'2_4anos.png'))]

def tela_de_start():
    global rodando
    global valor_continuar
    global continuar
    tela.fill(preto)
    fonte_start = pygame.font.SysFont('arial', 30, True, True)
    start = 'Pressione qualquer tecla para continuar'
    nada = ' '
    continuar = [fonte_start.render(start, False, (branco)),
                 fonte_start.render(nada, False, (preto))] 
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

def cutscene():
    global valor_cutscene
    global rodando
    global cena
    cena = [pygame.image.load(os.path.join('assets', 'cutscene00.png')),
            pygame.image.load(os.path.join('assets', 'cutscene01.png')),
            pygame.image.load(os.path.join('assets', 'cutscene02.png')),
            pygame.image.load(os.path.join('assets', 'cutscene03.png')),
            pygame.image.load(os.path.join('assets', 'cutscene04.png')),
            pygame.image.load(os.path.join('assets', 'cutscene05.png')),
            pygame.image.load(os.path.join('assets', 'cutscene06.png')),
            pygame.image.load(os.path.join('assets', 'cutscene07.png')),
            pygame.image.load(os.path.join('assets', 'cutscene08.png')),
            pygame.image.load(os.path.join('assets', 'cutscene09.png')),
            pygame.image.load(os.path.join('assets', 'cutscene10.png')),
            pygame.image.load(os.path.join('assets', 'cutscene11.png')),
            pygame.image.load(os.path.join('assets', 'cutscene12.png')),
            pygame.image.load(os.path.join('assets', 'cutscene13.png')),
            pygame.image.load(os.path.join('assets', 'cutscene14.png')),
            pygame.image.load(os.path.join('assets', 'cutscene15.png')),
            pygame.image.load(os.path.join('assets', 'cutscene16.png')),
            pygame.image.load(os.path.join('assets', 'cutscene17.png')),
            pygame.image.load(os.path.join('assets', 'cutscene18.png')),
            pygame.image.load(os.path.join('assets', 'cutscene19.png')),
            pygame.image.load(os.path.join('assets', 'cutscene20.png')),
            pygame.image.load(os.path.join('assets', 'cutscene21.png')),
            pygame.image.load(os.path.join('assets', 'cutscene22.png')),
            pygame.image.load(os.path.join('assets', 'cutscene23.png')),
            pygame.image.load(os.path.join('assets', 'cutscene24.png')),
            pygame.image.load(os.path.join('assets', 'cutscene25.png')),
            pygame.image.load(os.path.join('assets', 'cutscene26.png')),
            pygame.image.load(os.path.join('assets', 'cutscene27.png')),
            pygame.image.load(os.path.join('assets', 'cutscene28.png')),
            pygame.image.load(os.path.join('assets', 'cutscene29.png')),
            pygame.image.load(os.path.join('assets', 'cutscene30.png')),
            pygame.image.load(os.path.join('assets', 'cutscene31.png')),
            pygame.image.load(os.path.join('assets', 'cutscene32.png')),
            pygame.image.load(os.path.join('assets', 'cutscene33.png')),
            pygame.image.load(os.path.join('assets', 'cutscene34.png')),
            pygame.image.load(os.path.join('assets', 'cutscene35.png')),
            pygame.image.load(os.path.join('assets', 'cutscene36.png')),
            pygame.image.load(os.path.join('assets', 'cutscene37.png')),
            pygame.image.load(os.path.join('assets', 'cutscene38.png')),
            pygame.image.load(os.path.join('assets', 'cutscene39.png')),
            pygame.image.load(os.path.join('assets', 'cutscene40.png')),
            pygame.image.load(os.path.join('assets', 'cutscene41.png')),
            pygame.image.load(os.path.join('assets', 'cutscene42.png')),
            pygame.image.load(os.path.join('assets', 'cutscene43.png')),
            pygame.image.load(os.path.join('assets', 'cutscene44.png'))
            ]
    intro = cena[int(valor_cutscene)]
    intro = pygame.transform.scale(intro, (1200, 640))
    tela.blit(intro, (0, 0))

def train():
    paisagem = pygame.image.load(os.path.join('assets', 'paisagem.png'))
    paisagem = pygame.transform.scale(paisagem, (1200, 640))
    tela.blit(paisagem, (0, 0))
    trem = pygame.image.load(os.path.join('assets', 'trem.png'))
    trem = pygame.transform.scale(trem, (2800, 640))
    tela.blit(trem, (c, 0))

def tiro():
    barulho_tiro = pygame.mixer.Sound(os.path.join('assets', 'tiro.mp3'))
    barulho_tiro.play()

while (rodando == False):
    tela.fill(preto)
    relogio.tick(30)
    tela_de_start()
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                rodando = True

    valor_continuar += 0.1 

    pygame.display.flip()
            


while (rodando == True):
    relogio.tick(30)
    if gambiarra <= 0:
        cutscene()
        valor_cutscene += 0.25
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.flip()
        

    if (valor_cutscene == 5):
        tiro()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.flip()
    if (valor_cutscene == len(cena) - 1):
        gambiarra += 1
        if gambiarra2 <= 0:
            train()
            c -= 15
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            pygame.display.flip()
        if c + 2800 <= 0:
            gambiarra2 += 1
            tela.fill(verde)
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
                    global valor
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
                        global contador
                        contador +=1
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