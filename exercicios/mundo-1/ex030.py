"""Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

n1 = float(input('Digite um número qualquer: '))
if n1 % 2 == 0:
    print(f'{n1:.0f} é um número par!')
else:
    print(f'{n1:.0f} é um número ímpar!')
