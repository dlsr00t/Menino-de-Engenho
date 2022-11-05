import pygame
from pygame.locals import *
import os 
from variaveis import *



class Dialogo(pygame):
    
    def dialogo(ret1 = "ret_um", ret2 = "ret_dois", ret2_cord_a=200, ret2_cord_b = 281):
        ret1 = pygame.Rect(x, y, 50, 81)
        ret2 = pygame.Rect(a+ret2_cord_a, b+ret2_cord_b, 50, 81)
        global texto
        global texto_count
        if ret1.colliderect(ret2):
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



class Movimento():
    def esta_em_movimento():
        global valor
        global movimentando
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                valor += 0.25
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

    def sprite(sprite_name):
        global image_sprite
        image_sprite = [pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                        pygame.image.load(os.path.join('assets', sprite_name+ '1.png')),
                        pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                        pygame.image.load(os.path.join('assets', sprite_name+'2.png'))]



class Tela():

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

    def tela_de_end():
        pass

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



