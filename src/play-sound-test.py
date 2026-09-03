import pygame
import trackstart

pygame.mixer.init()
pygame.mixer.music.load(trackstart.m3) # Escolha de m1 até m13 para mudar a música
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

