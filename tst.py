import time
import pygame
import os
from pathlib import Path
import pafy
from pydub import AudioSegment
from time import sleep




pygame.init()
musicas = []
filename_filter = "*.mp3"
caminho_musicas = []
nome_curto = []
item = 0


for filename in Path("/home").rglob(filename_filter):
    if not filename.name in nome_curto:
        caminho_musicas.append(str(filename))
        nome_curto.append(filename.name)

for musica in nome_curto:
    print("[", item, "] ", musica)
    item+=1

escolha = int(input("escolha o numero da musica que vc deseja escutar: "))
musica = pygame.mixer.music.load(os.path.join(caminho_musicas[escolha]))
pygame.mixer.music.play()

while True:
    
    
    
    pass

