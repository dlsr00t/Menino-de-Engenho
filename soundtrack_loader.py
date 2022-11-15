import time
import pygame
import os
from pathlib import Path
import pafy
from pydub import AudioSegment
from time import sleep


do_it = str(input("Oque vc deseja fazer Baixar ou Tocar musicas?:  ")).lower()

def play(caminho = r'' ):
    pygame.init()
    musicas = []
    filename_filter = "*.mp3"
    caminho_musicas = []
    nome_curto = []
    item = 0
    try:
        for filename in Path(caminho).rglob(filename_filter):
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
    
    except KeyboardInterrupt:
        print("\nTchauuu ;)")


def load():
    print("\033[4;33m###ISSO IRA BAIXAR MUSICAS DO YOUTUBE!!!###\033[m")
    print("\033[1;31mEscrito por Foureyes\033[m\n\n")
    url = str(input("Por favor cole a url da musica do youtube que vc deseja: "))
    caminho = os.path.dirname(os.path.realpath(__file__))+"/"
    result = pafy.new(url)
    best_quality_video = result.getbestaudio("m4a")
    print(result.title)
    print(best_quality_video)
    best_quality_video.download(caminho)
    sleep(2)
    musica = AudioSegment.from_file(caminho+result.title+".m4a")
    musica.export(caminho+result.title+".mp3", format = "mp3")
    os.remove(caminho+result.title+".m4a")



if os.name == "nt":
    os.system("cls")
    if do_it == "tocar":
        play('C:\*')
    elif do_it == "baixar":
        load()

