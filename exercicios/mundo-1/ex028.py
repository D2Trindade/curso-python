"""Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep
n1 = randint(1, 5)
print('-=-' * 20)
print('Estou pensando em um número entre 0-5, tente adivinhar qual.')
print('-=-' * 20)
n2 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if n2 == n1:
    print(f'PARABÉNS! Eu pensei no número {n1}, você me venceu!')
else:
    print(f'ERROU! Eu pensei no número {n1} e não no {n2}.')
