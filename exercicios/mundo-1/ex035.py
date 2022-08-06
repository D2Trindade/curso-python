"""Exercício Python 035: Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não formar um triângulo."""

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
# if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
