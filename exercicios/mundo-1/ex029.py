"""Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

n1 = float(input('Qual é a velocidade atual do carro? '))
if n1 > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80km/h')
    print(f'Você deve pagar uma multa de R${(n1 - 80) * 7:.2f}')
print('Tenha um ótimo dia! Dirija com segurança!')

