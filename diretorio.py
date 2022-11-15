from pathlib import Path

base_path = r'/home'
filename_filter = "*.mp3"
caminho_musicas = []
nome_curto = []
item = 0

for filename in Path(base_path).rglob(filename_filter):
    #print(filename)
    if not filename.name in nome_curto:
        caminho_musicas.append(str(filename))
        nome_curto.append(filename.name)


for musica in nome_curto:
    print("[", item, "] ", musica)


escolha = int(input("Escolha o numero da musica que vc deseja escutar: ")






'''
import glob
path="/"

print("\nUsing glob.iglob()")
for file in glob.iglob(path,"*.py", recursive=True):
    print(file)
'''

'''
for item in diretorio:
    if item.is_file():
        print(item.name)
'''
