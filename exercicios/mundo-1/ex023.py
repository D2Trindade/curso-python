"""Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados."""

# Código feito por mim:

"""n1 = str(input('Informe um número (0-9999): '))
print(f'Analisando o número {n1}...')
print(f'Unidade: {n1[3]}')
print(f'Dezena: {n1[2]}')
print(f'Centena: {n1[1]}')
print(f'Milhar: {n1[0]}')"""

# Código aprimorado feito pelo professor:

n1 = int(input('Digite um número (0-9999): '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'Analisando o número {n1}...')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
