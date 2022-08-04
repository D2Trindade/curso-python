"""Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice

# CÓDIGO FEITO PELO PROFESSOR

'''a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno :')
alunos = a1, a2, a3, a4
print(f'O aluno selecionado foi {choice(alunos)}')'''

# CÓDIGO FEITO POR MIM

print('O professor da turma vai sortear um dos seus quatro alunos para apagar o quadro. \nQuem está participando'
      ' do sorteio é Diego, Gustavo, João e Maria.')
alunos = ['Diego', 'Gustavo', 'João', 'Maria']
print(f'O aluno escolhido para apagar o quadro foi o(a) {choice(alunos)}')