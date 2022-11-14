import time
import pygame
import os

pygame.init()

musica = pygame.mixer.music.load(os.path.join('assets', "Kanye West - Praise God (Audio)"+'.mp3'))
pygame.mixer.music.play(-1)
while True:
    pass