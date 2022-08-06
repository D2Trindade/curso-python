"""Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

# Código feito por mim:
"""n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = n1 if n1 > n2 and n1 > n3 else n2 if n2 > n1 and n2 > n3 else n3
menor = n1 if n1 < n2 and n1 < n3 else n2 if n2 < n1 and n2 < n3 else n3
print(f'Maior valor é {maior}')
print(f'Menor valor é {menor}')"""

# Código feito pelo professor:
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
