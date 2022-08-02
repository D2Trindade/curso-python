"""Exercício Python 005: Faça um programa que leia um número Inteiro
e mostre na tela o seu sucessor e seu antecessor."""

n1 = int(input('Digite um número : '))
print('O antecessor do número {} é {}'.format(n1, n1 - 1))
print('O sucessor do número {} é {}'.format(n1, n1 + 1))
