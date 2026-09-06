import os
os.environ["SDL_AUDIODRIVER"] = "pulseaudio"
import pygame
import random
import time

pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.init()

player = os.path.dirname(os.path.abspath(__file__))

band1 = os.path.join(player,"..", "src", "band1", "musicas")

musicas = []

for arquivo in os.listdir(band1):
    if arquivo.lower().endswith(".mp3"):
        caminho = os.path.join(band1, arquivo)
        musicas.append(caminho)
if not musicas:
    print("Nenhuma música MP3 foi encontrada!")
    pygame.quit()
    exit()

print(f"{len(musicas)} Músicas encontradas:")

random.shuffle(musicas)

for musica in musicas:
    print("TOCANDO: ", os.path.basename(musica))

    pygame.mixer.music.load(musica)

    pygame.mixer.music.set_volume(0.5)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

print("\nTodas as músicas foram reproduzidas!")

pygame.quit()
