"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date
ano = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: \033[36mMirim\033[m.')
elif idade <= 14:
    print('Classificação: \033[34mInfantil\033[m.')
elif idade <= 19:
    print('Classificação: \033[32mJúnior\033[m.')
elif idade <= 25:
    print('Classificação: \033[33mSênior\033[m.')
elif idade > 25:
    print('Classificação: \033[31mMaster\033[m.')
