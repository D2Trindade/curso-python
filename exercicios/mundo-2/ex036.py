"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado."""

casa = int(input('Qual o valor da casa? R$'))
salario = int(input('Qual é o valor do seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
if prestacao > 0.3 * salario:
    print('Empréstimo \033[31mNEGADO\033[m!')
else:
    print('Empréstimo \033[32mAPROVADO\033[m! Obrigado pela preferência.')

