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
pygame.init()

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



def dialogo(ret1 = "ret_um", ret2 = "ret_dois", ret2_cord_a=200, ret2_cord_b = 281, dialogo = mensagem):
    ret1 = pygame.Rect(x, y, 50, 81)
    ret2 = pygame.Rect(a+ret2_cord_a, b+ret2_cord_b, 50, 81)
    global texto
    global texto_count
    if ret1.colliderect(ret2):
        #tr(mega)
        if not texto:
            formatacao = fonte.render(nome, False, (255,255,255))
            tela.blit(formatacao, (a + 200, b + 150))   #a+175, b+150
        if texto == True and texto_count <= len(mensagem):
            formatacao = fonte.render(mensagem[texto_count-1], False, (0,0,0))
            tela.blit(formatacao, (a+200, b+150))

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
    global movimentando
    if event.type == QUIT:
        pygame.quit()
        exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
           ##valor += 0.25
            return True

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
            valor = 0
            return False

        '''
        if movimentando == True:
            valor += 0.25
        else:
            valor = 0
        '''



def mostrar(callback, fundo = preto):
    tela.fill(fundo)
    relogio.tick(30)
    callback()
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


def tr(callback, trilha = "mega", play = True):
    global jft
    global musica
    global block
    if play == True:
        pygame.init()
        
        if jft > 0:
            
            block = "nao pode tocar"
            print(block)
            return "ja ta tocando"
        
        try:
            musica = pygame.mixer.music.load(os.path.join('assets', trilha+'.mp3'))
            pygame.mixer.music.play(-1)
            callback()
        except pygame.error as er:
            if "No file" in str(er):
                print("\033[1;31mNao foi possivel encontrar a musica\033[m")
            else:
                print("\033[1;31m"+str(er)+"\033[m")
            
            exit()
    elif play == False:
        contadora(zerar=True)
        pygame.mixer.music.stop()
            
    
    

def contadora(zerar = False):
    global jft ###A variavel $jft significa --> Ja Foi Tocada? E se ela for zero significa que ainda nn foi tocada
    if zerar == True:
        jft = 0
        
    else:
        jft+=1
    #return jft



def tempo():
    global inicio
    fim = time.time()
    return fim-inicio



def cutscene(cena = "", estado_da_cena = True):
    global x
    global y
    global a
    global b
    global scene
    global movimentando
    global ultimo
 
    if cena == "esquerda":
        if x > a:
            x -= 4
            movimentando = True
            sprite("sprite_esquerda")
            ultimo = "sprite_esquerda"
            a += 4
        else:
            valor = 0

    elif cena == "direita":
        if x + 50 < a + 1200:
            x += 4
            movimentando = True
            sprite("sprite_direita")
            ultimo = "sprite_direita"
            a -= 4
        else:
            valor = 0

    elif cena == "cima":
        if y > b:
            y -= 4
            movimentando = True
            sprite("sprite_cima")
            ultimo = "sprite_cima"
            b += 4
        else:
            valor = 0

    elif cena == "baixo":
        if y + 81 < b + 640:
            y += 4
            movimentando = True
            sprite("sprite_baixo")
            ultimo = "sprite_baixo"
            b -= 4
        else:
            valor = 0

    elif cena == "diagonal superior esquerda":
        if y > b and x > a:
            y -= 4
            x -= 4
            movimentando = True
            sprite("sprite_cima")
            ultimo = "sprite_cima"
            b += 4
            a += 4
        else:
            valor = 0

    elif cena == "diagonal superior direita":
        if y > b:
            y -= 4
            x += 4
            movimentando = True
            sprite("sprite_cima")
            ultimo = "sprite_cima"
            b += 4
            a -= 4
        else:
            valor = 0

    elif cena == "diagonal inferior esquerda":
        if y + 81 < b + 640:
            y += 4
            x-=4
            movimentando = True
            sprite("sprite_baixo")
            ultimo = "sprite_baixo"
            b -= 4
            a+=4
        else:
            valor = 0


    elif cena == "diagonal inferior direita":
        if y + 81 < b + 640:
            y += 4
            x+=4
            movimentando = True
            sprite("sprite_baixo")
            ultimo = "sprite_baixo"
            b -= 4
            a-=4
        else:
            valor = 0
    if estado_da_cena == True:
        scene = True
    else:
        scene = False


while (rodando == False):
    mostrar(tela_de_start)

tr(contadora)
while (rodando == True):
    relogio.tick(30)
    tela.fill(branco)
    tela.blit(background, (a, b))
    tela.blit(npc, (a + 200, b + 200))
    sprite(ultimo)    
    dialogo()
    if tempo() >= 10 and jft > 0 and jfc == 0:
        contadora(zerar=True)
        pygame.mixer.music.stop()
        jfc+=1
    
    if tempo() >= 10 and jft == 0:
        tr(contadora, "Kanye West - Praise God (Audio)")


        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        movimentando = esta_em_movimento()         
        hook_para_dialogo()
        
    
        

    if pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_d] and scene == False:
        ultimo = ultimo

    elif pygame.key.get_pressed()[K_a] and scene == False:
        if x > a:
            x -= 4
            movimentando = True
            sprite("sprite_esquerda")
            ultimo = "sprite_esquerda"
            a += 4
        else:
            valor = 0

    elif pygame.key.get_pressed()[K_d] and scene == False:
        if x + 50 < a + 1200:
            x += 4
            movimentando = True
            sprite("sprite_direita")
            ultimo = "sprite_direita"
            a -= 4
        else:
            valor = 0


    if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_s] and scene == False:
        ultimo = ultimo

    elif pygame.key.get_pressed()[K_w] and scene == False:
        if y > b:
            y -= 4
            movimentando = True
            sprite("sprite_cima")
            ultimo = "sprite_cima"
            b += 4
        valor = 0

    elif pygame.key.get_pressed()[K_s] and scene == False:
        if y + 81 < b + 640:
            y += 4
            movimentando = True
            sprite("sprite_baixo")
            ultimo = "sprite_baixo"
            b -= 4
        else:
            valor = 0
    #if pygame.key.get_pressed()[K_t]:
    #cutscene("esquerda")
    
    
    movimento()

    if movimentando == False and contador == 0:
        instrucoes()
            
    '''
    ret_um = pygame.Rect(x, y, 50, 81)
    ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)
    if ret_um.colliderect(ret_dois):     
        tela.blit(nome_formatado, (a + 175, b + 150))
    '''
    
    #tela.blit(nome_formatado, (a + 175, b + 150))
    pygame.display.flip()
