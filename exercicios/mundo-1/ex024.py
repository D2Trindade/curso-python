""""Exercício Python 24: Crie um programa que leia o nome de
uma cidade diga se ela começa ou não com o nome “SANTO”."""

# Código feito por mim:

'''cidade = str(input('Digite em que cidade você nasceu: ')).strip().upper()
print('SANTO'.strip() in cidade)'''

# Código feito pelo professor:

cidade = str(input('Digite em que cidade você nasceu: ')).strip().upper()
print(cidade[:5] == 'SANTO'.upper())

