"""Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

peso = int(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso / (altura * altura)
print(f'O seu IMC é {IMC:.1f}')
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= IMC < 25:
    print('Parabéns, você está na faixa de peso ideal.')
elif 25 <= IMC < 30:
    print('Você está acima do peso.')
elif 30 <= IMC < 40:
    print('Você está com obesidade.')
elif IMC > 40:
    print('Você está com obesidade mórbida.')
