"""Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle
print('O mesmo professor agora quer sortear a ordem de apresentação do trabalho feito por seus alunos de outra turma.')
alunos = ['Gabriel', 'Kayo', 'Diego', 'Leo']
shuffle(alunos)
print(f'A ordem de apresentação vai ser: {alunos}')

