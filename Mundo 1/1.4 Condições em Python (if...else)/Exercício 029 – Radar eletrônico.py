# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Digite a velocidade do carro em Km/h: '))
if v > 80:
    print(f'\033[31mVocê foi multado. O valor a pagar é de R${7*(v-80):.2f}.')
    print('\033[33mDirija com atenção, tenha um bom dia.')
else:
    print('\033[33mDirija com atenção, tenha um bom dia.')
