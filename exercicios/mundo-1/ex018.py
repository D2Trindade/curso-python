"""Exercício Python 18: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

from math import radians, cos, sin, tan
n1 = float(input('Digite o valor do ângulo: '))
n1_rad = radians(n1)
print(f'O ângulo de {n1} tem o SENO de {sin(n1_rad):.2f}')
print(f'O ângulo de {n1} tem o CONSSENO de {cos(n1_rad):.2f}')
print(f'O ângulo de {n1} tem a TANGENTE de {tan(n1_rad):.2f}')
