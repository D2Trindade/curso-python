"""Exercício Python 008: Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros."""

n1 = float(input('Digite uma distância em metros: '))
print(f'A medida de {n1}m equivale a: ')
print(f'{n1 / 1000}km \n{n1 / 100}hm \n{n1 / 10}dam \n{n1 * 10:.0f}dm \n{n1 * 100:.0f}cm \n{n1 * 1000:.0f}mm')
