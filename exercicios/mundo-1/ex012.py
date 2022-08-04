"""Exercício Python 012: Faça um algoritmo que leia o preço de
um produto e mostre seu novo preço, com 5% de desconto."""

n1 = float(input('Insira o valor original do produto: '))
print(f'O novo valor do produto com 5% de desconto aplicado é: R${n1 - (n1 * 0.05):.2f}')
