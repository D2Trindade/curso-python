"""Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você."""

# Código feito por mim:

"""from random import choice
from time import sleep
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

player = int(input('Escolha sua jogada: '))
if player == 0:
    player = 'Pedra'
elif player == 1:
    player = 'Papel'
elif player == 2:
    player = 'Tesoura'
options = ['Pedra', 'Papel', 'Tesoura']
pc = choice(options)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print(f'O computador jogou {pc}.')
print(f'Você jogou {player}')
if player == 'Pedra' and pc == 'Tesoura':
    print('VOCÊ VENCEU!')
elif player == 'Pedra' and pc == 'Papel':
    print('VOCÊ PERDEU...')
elif player == 'Papel' and pc == 'Pedra':
    print('VOCÊ VENCEU!')
elif player == 'Papel' and pc == 'Tesoura':
    print('VOCÊ PERDEU...')
elif player == 'Tesoura' and pc == 'Papel':
    print('VOCÊ VENCEU!')
elif player == 'Tesoura' and pc == 'Pedra':
    print('VOCÊ PERDEU...')
elif player == 'Papel' and pc == 'Papel':
    print('EMPATOU.')
elif player == 'Pedra' and pc == 'Pedra':
    print('EMPATOU.')
elif player == 'Tesoura' and pc == 'Tesoura':
    print('EMPATOU.')"""

# Código feito pelo professor durante a correção do exercício:

from random import randint
from time import sleep
options = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
player = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print(f'Você jogou {options[player]}.')
print(f'O computador jogou {options[pc]}.')
if pc == 0:
    if player == 1:
        print('VOCÊ VENCEU!')
    elif player == 2:
        print('VOCÊ PERDEU...')
    elif player == 0:
        print('EMPATOU.')
elif pc == 1:
    if player == 2:
        print('VOCÊ VENCEU!')
    elif player == 0:
        print('VOCÊ PERDEU...')
    elif player == 1:
        print('EMPATOU.')
elif pc == 2:
    if player == 0:
        print('VOCÊ VENCEU!')
    elif player == 1:
        print('VOCÊ PERDEU...')
    elif player == 2:
        print('EMPATOU.')