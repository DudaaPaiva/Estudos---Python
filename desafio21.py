# Desafio para tocar uma música em Python
import pygame
pygame.init() #primeiro tem que iniciar o pygame
pygame.mixer.music.load('Forest.mp3') #nome da musica
pygame.mixer.music.play()
input()
pygame.event.wait() #comando para aguardar o evento acabar
