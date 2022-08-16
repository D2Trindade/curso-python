"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

n1 = float(input('Digite sua nota no teste: '))
n2 = float(input('Digite sua nota na prova: '))
media = (n1 + n2) / 2
print(f'Sua média final é {media}.')
if media < 5:
    print(f'Você foi \033[7mREPROVADO\033[m.')
elif 7 > media >= 5:
    print(f'Você está de \033[31mRECUPERAÇÃO\033[m.')
elif media >= 7.0:
    print(f'\033[32mParabéns, você passou!')
