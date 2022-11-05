import pygame
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
preto = (0,0,0)
rodando = False
valor_continuar = 0
contador = 0
inicio = time.time()
jft = 0
jfc = 0
scene = False