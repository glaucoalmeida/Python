# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

s = int(input('Qual será o valor sacado? R$ '))
d = 50
c = 0
a = s % d
while True:
    if s >= d:
        s -= d
        c += 1
    else:
        if c > 0:
            print(f'{c} cédulas de R$ {d}.')
        c = 0
        if d == 50:
            d = 20
        elif d == 20:
            d = 10
        elif d == 10:
            d = 1
        if s == 0:
            break
