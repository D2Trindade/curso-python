"""Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

# Código atualizado que ainda funciona (04/08/2022)

import playsound
playsound.playsound('ex021.mp3')

# Código desatualizado usado na aula

"""import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()"""
