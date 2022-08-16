"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

value = float(input('Valor das compras R$'))
print('''Formas de pagamento:
[ 1 ] Á vista
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] Até 12x no cartão''')
pay = str(input('Qual será a forma de pagamento? '))
if pay == '1':
    print('Você recebeu um desconto de 10% por pagar á vista em dinheiro.')
    print(f'O valor final da compra ficou em R${value - (value * 0.1):.2f}')
elif pay == '2':
    print('Você recebeu um desconto de 5% por pagar á vista no cartão.')
    print(f'O valor final da compra ficou em R${value - (value * 0.05):.2f}')
elif pay == '3':
    print('Você escolheu pagar em 2x no cartão.')
    print(f'O valor final da compra ficou em R${value:.2f}')
elif pay == '4':
    n1 = int(input('Quantas parcelas? '))
    if n1 > 12:
        print(f'Não é possível parcelar sua compra em {n1}x, tente novamente.')
    elif n1 < 3:
        print('Para essa opção é necessário parcelar em no mínimo 3x, use outra opção para parcelar em menos vezes.')
    else:
        print(f'Sua compra será parcelada em {n1}x de R${(value + value * 0.2) / n1:.2f} COM JUROS.')
        print(f'O valor final da compra ficou em R${value + (value * 0.2):.2f}')
else:
    print('\033[31mOpção inválida, tente novamente.')
