"""Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

a = float(input('Qual é o salário do funcionário? R$'))
if a > 1250.00:
    print(f'Seu novo salário é R${(a * 0.1) + a:.2f}')
else:
    print(f'Seu novo salário é R${(a * 0.15) + a:.2f}')
