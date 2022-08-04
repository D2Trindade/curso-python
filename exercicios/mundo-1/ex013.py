"""Exercício Python 013: Faça um algoritmo que leia o salário de
um funcionário e mostre seu novo salário, com 15% de aumento."""

n1 = float(input('Digite o valor do salário: R$'))
print(f'O valor do seu novo salário após o aumento é: R${n1 + (n1 * 0.15):.2f}')

