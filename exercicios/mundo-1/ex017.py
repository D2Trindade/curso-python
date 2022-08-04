"""Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""

from math import hypot
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(n1, n2):.2f}')






