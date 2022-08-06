"""Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

n1 = float(input('Qual é a distância da viagem? '))
print(f'Você está prestes a fazer uma viagem de {n1:.0f}Km.')
if n1 <= 200:
    print(f'E o preço da sua passagem será de R${n1 * 0.5:.2f}')
else:
    print(f'E o preço da sua passagem será de R${n1 * 0.45:.2f}')

# Outro método de fazer o mesmo código:

"""n1 = float(input('Qual é a distância da viagem? '))
n2 = n1 * 0.5 if n1 <= 200 else n1 * 0.45
print(f'Você está prestes a fazer uma viagem de {n1:.0f}Km.')
print(f'E o preço da sua passagem será de R${n2:.2f}')"""
