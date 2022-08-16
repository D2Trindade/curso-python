""""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
 escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão:
 [1] para converter para BINÁRIO
 [2] para converter para OCTAL
 [3] para converter para HEXADECIMAL''')
num2 = int(input('Sua opção: '))
if num2 == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif num2 == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif num2 == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print(f'Opção \033[31mINVÁLIDA\033[m. Tente novamente.')

