
from glob import glob
import pygame
from pygame.locals import *
from sys import exit
import os
import time
from variaveis import *


from pygame import mixer
import threading
from random import randint

pygame.display.set_caption('Menino do Engenho')

mixer.init()

pontos=0
sla = 0
gambiarra3 = 0
x_marrom = 900
y_marrom = 200
largura = 1200
altura = 640
x=largura/2
y=altura/2
#relogio=pygame.time.Clock()
#tela=pygame.display.set_mode((largura, altura))


rodando = False
valor_continuar = 0
contador = 0
valor_cutscene = 0
gambiarra = 0
gambiarra2 = 0
c = 1300
a = 0 
b = 0
x_trem_voltando = -2800
gambiarra4 = 0
contador_som_trem2 = 0

posicoesx = []
posicoesy = []
nnpode = [[a + 200, b + 200],[a + 300, b + 400],[a+400, b+50],[a+700, b+50],[a+900, b+350]]
contador_som_trem = 0

donda = ''
def sprite(sprite_name, age):
    global image_sprite
    image_sprite = [pygame.image.load(os.path.join('assets', sprite_name+'_'+age+'anos.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+ '1_'+age+'anos.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'_'+age+'anos.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'2_'+age+'anos.png'))]

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

def train2():
    paisagem_dia = pygame.image.load(os.path.join('assets', 'paisagem_dia.png'))
    paisagem_dia = pygame.transform.scale(paisagem_dia, (1200, 640))
    tela.blit(paisagem_dia, (0, 0))
    trem_voltando = pygame.image.load(os.path.join('assets', 'trem_voltando.png'))
    trem_voltando = pygame.transform.scale(trem_voltando, (2800, 640))
    tela.blit(trem_voltando, (x_trem_voltando, 0))

def tiro():
    barulho_tiro = pygame.mixer.Sound(os.path.join('assets', 'tiro.mp3'))
    barulho_tiro.play()


def dialogo(info, contadora):
    global ret1
    global ret2
    ret1 = pygame.Rect(x, y, 50, 81)
    #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
    ret2 = pygame.Rect(a+info["posicao"][0]+3, b+info["posicao"][1]+81, 45, 81)
    global texto_tio_juca
    global texto_vo_jose_paulino
    global texto_count
    global texto_tia_maria
    global texto_tia_sinhazinha
    global primos
    global texto_prima_maria_clara


    global uncolliderect

    global cont_tio_juca
    global cont_vo_jose_paulino
    global cont_tia_maria
    global cont_tia_sinhazinha
    global cont_primos
    global cont_prima_maria_clara
    global falou
    global fases
    if contadora == "cont_tio_juca":
        if ret1.colliderect(ret2):
            #print(info["tst"])
            if not texto_tio_juca:
                formatacao = fonte.render(info["nome"], False, (0,0,0))
                tela.blit(formatacao, (a+info["posicao"][0]-7, b+info["posicao"][1]-30))
            if texto_tio_juca == True and cont_tio_juca <= len(info["mensagem"][fases]):
                formatacao = fonte.render(info["mensagem"][fases][cont_tio_juca-1], False, (0,0,0))
                if fases == 1 and cont_tio_juca ==2 :
                    tela.blit(formatacao, (a+info["posicao"][0]-90, b+info["posicao"][1]-30))
                else:
                    tela.blit(formatacao, (a+info["posicao"][0]-200, b+info["posicao"][1]-30))
    if contadora == "cont_vo_jose_paulino":
        if ret1.colliderect(ret2):
            #print(info["tst"])
            if not texto_vo_jose_paulino:
                formatacao = fonte.render(info["nome"], False, (0,0,0))
                tela.blit(formatacao, (a+info["posicao"][0]-40, b+info["posicao"][1]-30))
            if texto_vo_jose_paulino == True and cont_vo_jose_paulino <= len(info["mensagem"][fases]):
                formatacao = fonte.render(info["mensagem"][fases][cont_vo_jose_paulino-1], False, (0,0,0))
                if cont_vo_jose_paulino ==1 or fases==1:
                    tela.blit(formatacao, (a+info["posicao"][0]-90, b+info["posicao"][1]-30))
                else:
                    tela.blit(formatacao, (a+info["posicao"][0]-200, b+info["posicao"][1]-30))
    if contadora == "cont_tia_maria":
        if ret1.colliderect(ret2):
            #print(info["tst"])
            if not texto_tia_maria:
                formatacao = fonte.render(info["nome"], False, (0,0,0))
                tela.blit(formatacao, (a+info["posicao"][0]-15, b+info["posicao"][1]-30))
            if texto_tia_maria == True and cont_tia_maria <= len(info["mensagem"][fases]):
                formatacao = fonte.render(info["mensagem"][fases][cont_tia_maria-1], False, (0,0,0))
                if cont_tia_maria == 1:
                    tela.blit(formatacao, (a+info["posicao"][0]-80, b+info["posicao"][1]-30))
                else:
                    tela.blit(formatacao, (a+info["posicao"][0]-110, b+info["posicao"][1]-30))      
    if contadora == "cont_tia_sinhazinha":
        if ret1.colliderect(ret2):
            #print(info["tst"])
            if not texto_tia_sinhazinha:
                formatacao = fonte.render(info["nome"], False, (0,0,0))
                tela.blit(formatacao, (a+info["posicao"][0]-35, b+info["posicao"][1]-30))
            if texto_tia_sinhazinha == True and cont_tia_sinhazinha <= len(info["mensagem"][fases]):
                formatacao = fonte.render(info["mensagem"][fases][cont_tia_sinhazinha-1], False, (0,0,0))

                tela.blit(formatacao, (a+info["posicao"][0]-140, b+info["posicao"][1]-30))
    if contadora == "cont_primos":
        ret2 = pygame.Rect(a+info["posicao"][0]+3, b+info["posicao"][1]+81, 90, 81)
        if ret1.colliderect(ret2):
            #print(info["tst"])

            if not texto_primos:
                formatacao = fonte.render(info["nome"], False, (0,0,0))
                tela.blit(formatacao, (a+info["posicao"][0]+15, b+info["posicao"][1]-65))
            if texto_primos == True and cont_primos <= len(info["mensagem"][fases]):
                formatacao = fonte.render(info["mensagem"][fases][cont_primos-1], False, (0,0,0))
                
                if fases == 1 and cont_primos == 2:
                    tela.blit(formatacao, (a+info["posicao"][0]-140, b+info["posicao"][1]-65))
                else:
                    tela.blit(formatacao, (a+info["posicao"][0]-70, b+info["posicao"][1]-60))
    
    if contadora == "cont_prima_maria_clara":
        if ret1.colliderect(ret2):
            #print(info["tst"])
            if not texto_prima_maria_clara:
                formatacao = fonte.render(info["nome"], False, (0,0,0))
                tela.blit(formatacao, (a+info["posicao"][0]-35, b+info["posicao"][1]-30))
            if texto_prima_maria_clara == True and cont_prima_maria_clara <= len(info["mensagem"]):
                formatacao = fonte.render(info["mensagem"][cont_prima_maria_clara-1], False, (0,0,0))
                if cont_prima_maria_clara == 1:
                    tela.blit(formatacao, (a+info["posicao"][0]-35, b+info["posicao"][1]-30))
                else:
                    tela.blit(formatacao, (a+info["posicao"][0]-140, b+info["posicao"][1]-30))


    #if texto_count > len(info["mensagem"]):
    #if texto_count > len(info["mensagem"]):
    #    texto_count = 0
    #    texto = False
    #    #print("zerado")
    #if not ret1.colliderect(ret2) and uncolliderect == 0:
    #    texto_count = 0
    #    texto = False  
    #    print("zerado")  
    #    uncolliderect += 1

   
def zeradora(info, contadora):
    global texto_tio_juca
    global texto_vo_jose_paulino
    global texto_count
    global texto_tia_maria
    global texto_tia_sinhazinha
    global texto_primos
    global texto_prima_maria_clara
    global ret1
    global ret2
    global uncolliderect
    
    global cont_tio_juca
    global cont_vo_jose_paulino
    global cont_tia_maria
    global cont_tia_sinhazinha
    global cont_primos
    global cont_prima_maria_clara
    global falou
    #if texto_count == len(info["mensagem"]):
    #    uncolliderect = 0
    if contadora == "cont_tio_juca":
        ret1 = pygame.Rect(x, y, 50, 81)
        #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
        ret2 = pygame.Rect(a+info["posicao"][0], b+info["posicao"][1]+81, 50, 81)        
        if cont_tio_juca >= len(info["mensagem"][fases]):
            falou["tio_juca"]=True
        if cont_tio_juca > len(info["mensagem"][fases]):
        #if texto_count > len(info["mensagem"]):
            cont_tio_juca = 0
            texto_tio_juca = False
            

            print("zerado")
        
        if not ret1.colliderect(ret2):
            #info["contadora"] = 0
            cont_tio_juca = 0
            texto_tio_juca = False  
            #print("zerado")  
            #uncolliderect += 1
        
        #info["tst"] += 1
    if contadora == "cont_vo_jose_paulino":
        ret1 = pygame.Rect(x, y, 50, 81)
        #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
        ret2 = pygame.Rect(a+info["posicao"][0], b+info["posicao"][1]+81, 50, 81)    
        if cont_vo_jose_paulino >= len(info["mensagem"][fases]):
            falou["vo_jose_paulino"] = True

        if cont_vo_jose_paulino > len(info["mensagem"][fases]):
        #if texto_count > len(info["mensagem"]):
            cont_vo_jose_paulino = 0
            texto_vo_jose_paulino = False
            
            #print("zerado")
        
        if not ret1.colliderect(ret2):
            #info["contadora"] = 0
            cont_vo_jose_paulino = 0
            texto_vo_jose_paulino = False  
            #print("zerado")  
            #uncolliderect += 1
        
        #info["tst"] += 1

    if contadora == "cont_tia_maria":
        ret1 = pygame.Rect(x, y, 50, 81)
        #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
        ret2 = pygame.Rect(a+info["posicao"][0], b+info["posicao"][1]+81, 50, 81)    
        if cont_tia_maria >= len(info["mensagem"][fases]):
            falou["tia_maria"] = True
        if cont_tia_maria > len(info["mensagem"][fases]):
        #if texto_count > len(info["mensagem"]):
            cont_tia_maria = 0
            texto_tia_maria = False
            
            #print("zerado")
        
        if not ret1.colliderect(ret2):
            #info["contadora"] = 0
            cont_tia_maria = 0
            texto_tia_maria = False  
            #print("zerado")  
            #uncolliderect += 1
        
        #info["tst"] += 1
    if contadora == "cont_tia_sinhazinha":
        ret1 = pygame.Rect(x, y, 50, 81)
        #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
        ret2 = pygame.Rect(a+info["posicao"][0], b+info["posicao"][1]+81, 50, 81)    
        if cont_tia_sinhazinha >= len(info["mensagem"][fases]):
            falou["tia_sinhazinha"] = True
        if cont_tia_sinhazinha > len(info["mensagem"][fases]):
        #if texto_count > len(info["mensagem"]):
            cont_tia_sinhazinha = 0
            texto_tia_sinhazinha = False
            
            #print("zerado")
        
        if not ret1.colliderect(ret2):
            #info["contadora"] = 0
            cont_tia_sinhazinha = 0
            texto_tia_sinhazinha = False  
            #print("zerado")  
            #uncolliderect += 1
        
        #info["tst"] += 1
    if contadora == "cont_primos":
        ret1 = pygame.Rect(x, y, 50, 81)
        #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
        ret2 = pygame.Rect(a+info["posicao"][0], b+info["posicao"][1]+81, 100, 81)    
        if cont_primos >= len(info["mensagem"][fases]):
            falou["primos"] = True
        if cont_primos > len(info["mensagem"][fases]):
        #if texto_count > len(info["mensagem"]):
            cont_primos = 0
            texto_primos = False
            falou["primos"] = True
            #print("zerado")
        
        if not ret1.colliderect(ret2):
            #info["contadora"] = 0
            cont_primos = 0
            texto_primos = False  
            #print("zerado")  
            #uncolliderect += 1
        
        #info["tst"] += 1

    if contadora == "cont_prima_maria_clara":
        ret1 = pygame.Rect(x, y, 50, 81)
        #ret2 = pygame.Rect(a + 200, b + 281, 50, 81)
        ret2 = pygame.Rect(a+info["posicao"][0], b+info["posicao"][1]+81, 100, 81)    
        if cont_prima_maria_clara >= len(info["mensagem"]):
            falou["prima_maria_clara"] = True
        if cont_prima_maria_clara > len(info["mensagem"]):
        #if texto_count > len(info["mensagem"]):
            cont_prima_maria_clara = 0
            texto_prima_maria_clara = False
            falou["prima_maria_clara"] = True
            #print("zerado")
        
        if not ret1.colliderect(ret2):
            #info["contadora"] = 0
            cont_prima_maria_clara = 0
            texto_prima_maria_clara = False  
            #print("zerado")  
            #uncolliderect += 1
        
        #info["tst"] += 1


def hook(info, contadora):
    global texto_tio_juca
    global texto_vo_jose_paulino
    global texto_count
    global texto_tia_maria
    global texto_tia_sinhazinha
    global texto_primos
    global texto_prima_maria_clara

    global cont_tio_juca
    global cont_vo_jose_paulino
    global cont_tia_maria
    global cont_tia_sinhazinha
    global cont_primos
    global cont_prima_maria_clara
    global ret1
    global ret2
    global falou
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
            if contadora == "cont_tio_juca":
            

                        ret1 = pygame.Rect(x, y, 50, 81)
                        ret2 = pygame.Rect(a + info["posicao"][0], b + info["posicao"][1]+81, 50, 81)             
                        if ret1.colliderect(ret2) and cont_tio_juca <= len(info["mensagem"][fases]):
                            #tela.blit(texto_formatado, (a + 175, b + 150))
                            texto_tio_juca = True
                            cont_tio_juca += 1
                            #info["tst"] += 1
                            #print(info["tst"])
            elif contadora == "cont_vo_jose_paulino":
            

                        ret1 = pygame.Rect(x, y, 50, 81)
                        ret2 = pygame.Rect(a + info["posicao"][0], b + info["posicao"][1]+81, 50, 81)             
                        if ret1.colliderect(ret2) and cont_vo_jose_paulino <= len(info["mensagem"][fases]):
                            #tela.blit(texto_formatado, (a + 175, b + 150))
                            texto_vo_jose_paulino = True
                            cont_vo_jose_paulino += 1
                            #info["tst"] += 1
                            #print(info["tst"])
            elif contadora == "cont_tia_maria":
                        ret1 = pygame.Rect(x, y, 50, 81)
                        ret2 = pygame.Rect(a + info["posicao"][0], b + info["posicao"][1]+81, 50, 81)             
                        if ret1.colliderect(ret2) and cont_tia_maria <= len(info["mensagem"][fases]):
                            #tela.blit(texto_formatado, (a + 175, b + 150))
                            texto_tia_maria = True
                            cont_tia_maria += 1
                            #info["tst"] += 1
                            #print(info["tst"])           
            elif contadora == "cont_tia_sinhazinha":
                        ret1 = pygame.Rect(x, y, 50, 81)
                        ret2 = pygame.Rect(a + info["posicao"][0], b + info["posicao"][1]+81, 50, 81)             
                        if ret1.colliderect(ret2) and cont_tia_sinhazinha <= len(info["mensagem"][fases]):
                            #tela.blit(texto_formatado, (a + 175, b + 150))
                            texto_tia_sinhazinha = True
                            cont_tia_sinhazinha += 1
                            #info["tst"] += 1
                            #print(info["tst"]) 
            elif contadora == "cont_primos":
                        ret1 = pygame.Rect(x, y, 50, 81)
                        ret2 = pygame.Rect(a + info["posicao"][0], b + info["posicao"][1]+81, 100, 81)             
                        if ret1.colliderect(ret2) and cont_primos <= len(info["mensagem"][fases]):
                            #tela.blit(texto_formatado, (a + 175, b + 150))
                            texto_primos = True
                            cont_primos += 1
                            #info["tst"] += 1
                            #print(info["tst"]) 
            elif contadora == "cont_prima_maria_clara":
            

                        ret1 = pygame.Rect(x, y, 50, 81)
                        ret2 = pygame.Rect(a + info["posicao"][0], b + info["posicao"][1]+81, 50, 81)             
                        if ret1.colliderect(ret2) and cont_prima_maria_clara <= len(info["mensagem"]):
                            #tela.blit(texto_formatado, (a + 175, b + 150))
                            texto_prima_maria_clara = True
                            cont_prima_maria_clara += 1
                            #info["tst"] += 1
                            #print(info["tst"])



def movimento():
    global valor
    global movimentando
    global image_sprite
    global imagem
    
    valor += 0.25 if movimentando == True else 0

    '''
    if movimentando == True:
        valor += 0.25
    else:
        valor = 0
    '''
    #movimentando = esta_em_movimento()

    if valor >= len(image_sprite):
        valor = 0

    imagem = image_sprite[int(valor)]
    imagem = pygame.transform.scale(imagem, (50, 81))

    tela.blit(imagem, (x, y))



while (rodando == False):
    if heartless == False and rodando == False:
        musica = pygame.mixer.music.load(os.path.join('assets','Kanye West - Heartless (8-bit Cover).mp3'))
        pygame.mixer.music.play()
        heartless = True
    tela.fill(preto)
    relogio.tick(30)
    tela_de_start()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            rodando = True
            pygame.mixer.music.stop()

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
            if event.type == KEYDOWN:
                valor_cutscene = len(cena) - 1
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
            while contador_som_trem == 0:
                trem_som = pygame.mixer.Sound(os.path.join('assets', 'trem.wav'))
                trem_som.play()
                contador_som_trem+=1
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    c = -2800
            pygame.display.flip()
        if c + 2800 <= 0:
            gambiarra2 += 1
    
        


            if fases == 0:
                tela.fill(verde)
                tela.blit(background, (a, b))
                tela.blit(tio_juca, (a + 200, b + 200))
                tela.blit(vo_jose_paulino, (a+300, b+400))
                tela.blit(tia_maria, (a+400, b+50))
                tela.blit(tia_sinhazinha, (a+700, b+50))
                tela.blit(primos, (a+900,b+300))
                sprite(ultimo, "4")
                dialogo(info_tio_juca, "cont_tio_juca")
                zeradora(info_tio_juca, "cont_tio_juca")
                dialogo(info_vo_jose_paulino, "cont_vo_jose_paulino")
                zeradora(info_vo_jose_paulino, "cont_vo_jose_paulino")
                dialogo(info_tia_maria, "cont_tia_maria")
                zeradora(info_tia_maria, "cont_tia_maria")
                dialogo(info_tia_sinhazinha, "cont_tia_sinhazinha")
                zeradora(info_tia_sinhazinha, "cont_tia_sinhazinha")
                dialogo(info_primos, "cont_primos")
                zeradora(info_primos, "cont_primos")
            elif fases == 1:
                
            
                #largura = 1200
                #altura = 640
                #x=largura/2
                #y=altura/2
                #imagem = pygame.transform.scale(imagem, (50, 81))
                #tela.blit(imagem, (x, y))
                tela.fill(verde)
                tela.blit(background, (a, b))
                tela.blit(tio_juca, (a + 200, b + 200))
                tela.blit(vo_jose_paulino, (a+300, b+400))
                tela.blit(tia_maria, (a+400, b+50))
                tela.blit(tia_sinhazinha, (a+700, b+50))
                tela.blit(primos, (a+900,b+300))
                tela.blit(prima_maria_clara, (((a+650, b+450))))
                sprite(ultimo, "8")
                dialogo(info_tio_juca, "cont_tio_juca")
                zeradora(info_tio_juca, "cont_tio_juca")
                dialogo(info_vo_jose_paulino, "cont_vo_jose_paulino")
                zeradora(info_vo_jose_paulino, "cont_vo_jose_paulino")
                dialogo(info_tia_maria, "cont_tia_maria")
                zeradora(info_tia_maria, "cont_tia_maria")
                dialogo(info_tia_sinhazinha, "cont_tia_sinhazinha")
                zeradora(info_tia_sinhazinha, "cont_tia_sinhazinha")
                dialogo(info_primos, "cont_primos")
                zeradora(info_primos, "cont_primos")
                dialogo(info_prima_maria_clara, "cont_prima_maria_clara") 
                zeradora(info_prima_maria_clara, "cont_prima_maria_clara")       
        
        
        
        
            elif fases == 2:
                tela.fill(verde)
                tela.blit(background, (a, b))
                tela.blit(tio_juca, (a + 200, b + 200))
                tela.blit(vo_jose_paulino, (a+300, b+400))
                #tela.blit(tia_maria, (a+400, b+50))
                tela.blit(tia_sinhazinha, (a+700, b+50))
                tela.blit(primos, (a+900,b+300))
                sprite(ultimo, "12")
                #time.sleep(1)
                dialogo(info_tio_juca, "cont_tio_juca")
                zeradora(info_tio_juca, "cont_tio_juca")
                dialogo(info_vo_jose_paulino, "cont_vo_jose_paulino")
                zeradora(info_vo_jose_paulino, "cont_vo_jose_paulino")
                #dialogo(info_tia_maria, "cont_tia_maria")
                #zeradora(info_tia_maria, "cont_tia_maria")
                dialogo(info_tia_sinhazinha, "cont_tia_sinhazinha")
                zeradora(info_tia_sinhazinha, "cont_tia_sinhazinha")
                dialogo(info_primos, "cont_primos")
                zeradora(info_primos, "cont_primos")
            
        
            while (fases == 3):###FIM DO JOGO
                if gambiarra4 <= 0:
                    train2()
                    x_trem_voltando += 15
                    while contador_som_trem2 == 0:
                        trem_som2 = pygame.mixer.Sound(os.path.join('assets', 'trem.wav'))
                        trem_som2.play()
                        contador_som_trem2+=1
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            x_trem_voltando = 1200
                    pygame.display.flip()
                if x_trem_voltando == 1200:
                    print('acabou')
                    gambiarra4 += 1
                    exit()
                if x_trem_voltando > 1200:
                    musica2 = pygame.mixer.music.load(os.path.join('assets','Kanye West - Heartless (8-bit Cover).mp3'))
                    pygame.mixer.music.play()
                    

        
        
        
        
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        pontos = 0
                        gambiarra3 = 0
                        aparecer = True
                def is_moving():
                    global valor
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                            #movimentando = False
                            valor = 0
                            return False
                movimentando = is_moving()
                hook(info_tio_juca, "cont_tio_juca")
                hook(info_vo_jose_paulino, "cont_vo_jose_paulino")
                hook(info_tia_maria, "cont_tia_maria")
                hook(info_tia_sinhazinha, "cont_tia_sinhazinha")
                hook(info_primos, "cont_primos")
                hook(info_prima_maria_clara, "cont_prima_maria_clara")
        
            
            if pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_d]:
                ultimo = ultimo
        
        
            
            elif pygame.key.get_pressed()[K_a]:    
                if x > a :
                    x -= 4
                    movimentando = True
                    #sprite("sprite_esquerda")
                    ultimo = "sprite_esquerda"
                    a += 4
                    donda = 'a'
        
        
                #else:
                    #print("colidiu")
                '''
                if ret1.collidelist(lista_colisao)>=0 and donda == 'a':
                    x=x+4
                    print("colidiu")
                    void = True
                '''
            elif pygame.key.get_pressed()[K_d]:
                if x + 50 < a + 1200 :
                    x += 4
                    movimentando = True
                    #sprite("sprite_direita")
                    ultimo = "sprite_direita"
                    a -= 4
                    donda = 'd'
                    #print("ret2: ", ret2)
                    #print("ret1: ", ret1)
                #else:
                    #print(ret1.collidelist(lista_colisao))
                '''
                if ret1.collidelist(lista_colisao)>=0 and donda == 'd':
                    x=x-4
                    print("colidiu")
                    void = True
                '''
        
            if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_s]:
                ultimo = ultimo
            
            elif pygame.key.get_pressed()[K_w]:
            
                
                #if donda == 'a' and ret1.collidelist(lista_colisao)>=0:
                #s    pass 
                # so pra ficar registrado se eu der um cntrl z
        
                if y > b :
                    #sprite("sprite_cima")
                    ultimo = "sprite_cima"
                    #print("to aqui")
                    y -= 4
                    movimentando = True
                    donda = 'w'
                    
                    b += 4
                    #donda = 'w'
        
            elif pygame.key.get_pressed()[K_s]:
                if y + 81 < b + 640 :
                    #sprite("sprite_baixo")
                    ultimo = "sprite_baixo"
                    y += 4
                    movimentando = True
                    donda = 's'
                    b-=4
        
        
                '''
                if ret1.collidelist(lista_colisao)>=0 and donda == 's':
                    y=y-5
                    print("colidiu")
                    void = True
                '''
        
            '''
            if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_d]:
                if x + 50 < a + 1200 and y > b and not ret1.collidelist(lista_colisao)>=0:
                    x += 4
                    y -= 4
                    movimentando = True
                    sprite("sprite_cima")
                    ultimo = "sprite_cima"
            '''        
        
            
            '''
            #movimento()
            if ret1.collidelist(lista_colisao)>=0 and donda == 'a' :
                #x=x+4
                #print("colidiu")
                movimentando = False
                bateu = 'esquerda'
                print("colidiu: ", donda)
            elif ret1.collidelist(lista_colisao)>=0 and donda == 'd':
                #x=x-5
                #print("colidiu")
                movimentando = False
                bateu='direita'
                print("colidiu: ", donda)
            elif ret1.collidelist(lista_colisao)>=0 and donda == 'w':
                #y=y+5
                #print("colidiu")
                movimentando = False
                bateu = 'cima'
                print("colidiu: ", donda)
            elif ret1.collidelist(lista_colisao)>=0 and donda == 's':
                #y=y-5
                #print("colidiu")
                movimentando = False
                bateu ='baixo'
                print("colidiu: ", donda)
            #print(ret1.collidelist(lista_colisao))
            #print(ret2)
            #print(primos.get_rect())
            #print(donda)
            #print(ret1)
            '''
        
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
            if (False in falou.values()):
                pass
            else:
                passa = True
                print("haha")
                relogio.tick(30)
                mensagemc = f'Canários: {pontos}'
                texto_formatado = fonte.render(mensagemc,False,(0, 0, 0))
                texto_rect = texto_formatado.get_rect()
                texto_rect.center = (largura/2, 100)
                #relogio.tick(120)
                #tela.fill((0,200,0))
                ret_azul = pygame.Rect(x, y, 50, 81)
                ret_marrom = pygame.Rect(a+x_marrom,b+y_marrom, 32, 32)
                '''
                if ret_azul.colliderect(ret_marrom):
                    x_marrom=randint(40,1100)
                    y_marrom=randint(50,550)
                    pontos+=1
                    sla +=1
                    tela.blit(texto_formatado, texto_rect)
                '''
                if ret_azul.colliderect(ret_marrom):
                        #print("so pra ver")
                        #x_marrom=randint(40,1100)
                        #y_marrom=randint(50,550)
                        x_marrom = randint(40, 1100)
                        pontos+=1
                        sla+=1
                        for d in nnpode:
                            #print(c[0])
                            posicoesx.append(d[0])
                        #print(posicoesx)
                        if x_marrom in posicoesx:
                            #print("valor igual")
                            posicoesx = []
                        #else:
                        #    print("passou: ",x_marrom)
                        y_marrom = randint(50, 550)
                        for d in nnpode:
                            posicoesy.append(d[1])
                        #print(posicoesy)
                        if y_marrom in posicoesy:
                            print("valor igual")
                            posicoesy = []
                        #else:
                        #    print("passou(y): ",y_marrom)
                if pontos == 0 and aparecer == True:
                    x_marrom = 900 
                    y_marrom = 200
                    aparecer = False
                    print(aparecer)
                    texto_formatado = fonte.render(nada, False, (255,255,255))
                elif pontos >= 3:
                    x_marrom = 900 
                    y_marrom = 200
                    
                    pontos = 0
                    fases+=1
                    a = 0
                    b = 0
                    x = largura/2
                    y = altura/2
                    #time.sleep(1)
                    falou = {
                    "tio_juca":False,
                    "vo_jose_paulino":False,
                    "tia_maria":False,
                    "tia_sinhazinha":False,
                    "primos":False,
                    "prima_maria_clara":False
                    }
                    if fases == 2:
                        falou.pop("tia_maria")
                        falou.pop("prima_maria_clara")
                    aparecer = False
                    passa = False
                    
                
                tela.blit(canario, (a+x_marrom, b+y_marrom))
                if pontos > 0 :
                    tela.blit(texto_formatado, texto_rect)
        
                #sprite(ultimo)
        
                #tela.blit(nome_formatado, (a + 175, b + 150))
                print(fases)
            pygame.display.flip()
        
