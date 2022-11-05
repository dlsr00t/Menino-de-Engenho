import pafy
from pydub import AudioSegment
import os
from time import sleep

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

print("\033[4;33m###ESSE PROGRAMA BAIXA MUSICAS DO YOUTUBE!!!###\033[m")
print("\033[1;31mEscrito por Foureyes\033[m\n\n")
url = str(input("Por favor cole a url da musica: "))
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

