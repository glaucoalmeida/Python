# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

b = 0
from random import randint
while True:
    j = int(input('Digite um número: '))
    c = randint (0,10)
    a = c + j
    s = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    while s not in 'PI':
        s = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    print('-=' * 40)
    print (f'O jogador digitou {j} e o computador escolheu {c}. A soma entre eles é {a}.')
    if s == 'P' and a % 2 == 0:
        print ('Jogador venceu.')
        print('-=' * 40)
        b += 1
    elif s == 'I' and a % 2 != 0:
        print ('Jogador venceu.')
        print('-=' * 40)
        b += 1
    else:
        print ('Computador venceu.')
        print('-=' * 40)
        break
print (f'O jogador venceu {b} partidas.')
print ('-='*40)
