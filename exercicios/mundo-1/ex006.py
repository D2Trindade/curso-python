"""Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

n1 = int(input('Digite um número: '))
print('O dobro de {} vale {} \nO triplo de {} vale {}'.format(n1, n1 * 2, n1, n1 * 3))
print('A raiz quadrada de {} é igual a {:.2f}'.format(n1, n1 ** (1/2)))

