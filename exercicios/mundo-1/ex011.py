"""Exercício Python 011: Faça um programa que leia a largura e a altura
de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área
de 2 metros quadrados."""

n1 = float(input('Digite quantos metros de altura tem a parede: '))
n2 = float(input('Agora digite a largura da parede em metros: '))
a = n1 * n2
print('A área da parede é de {}m²'.format(a))
print(f'Serão necessários {a / 2} litros de tinta para pintar essa parede.')


