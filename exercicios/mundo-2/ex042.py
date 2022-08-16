"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

print('-=-=-' * 10)
print('\033[33mANALISADOR DE TRIÂNGULOS 2.0\033[m')
print('-=-=-' * 10)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os valores podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO.')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('ISÓSCELES.')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO.')
else:
    print('Os valores não podem formar um triângulo.')