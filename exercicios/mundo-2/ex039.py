"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se
alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
o tempo que falta ou que passou do prazo."""

from datetime import date

# Código feito por mim

"""anonascimneto = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonascimneto
print(f'Quem nasceu em {anonascimneto} tem {idade} anos em {anoatual}.')
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {anoatual - (idade - 18)} ')
elif idade == 18:
    print(f'Você já tem 18 anos e deve realizar seu alistamento esse ano.')
else:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento.')
    print(f'Seu alistamento será em {anonascimneto + 18}.')"""

# Código feito pelo professor durante a correção do exercício

ano = date.today().year
genero = str(input('''
[ M ] = Masculino
[ F ] = Feminino
Qual é o seu sexo? ''')).strip().upper()

nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {ano}.')
if genero == 'F':
    print(f'Você nasceu em {nasc} e tem {ano - nasc} anos, mas não precisa se alistar por ser mulher.')
elif genero == 'M' and idade > 18:
    print(f'Você já deveria ter feito seu alistamento há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano - (idade - 18)}')
elif genero == 'M' and idade == 18:
    print(f'Você já tem 18 anos e deve realizar seu alistamento ainda esse ano.')
elif genero == 'M' and idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você realizar seu alistamento.')
    print(f'Seu alistamento será em {nasc + 18}')
elif genero != 'M' or genero != 'F':
    print('\033[31mOpção de gênero inválida, seu esquisito\033[m.')
