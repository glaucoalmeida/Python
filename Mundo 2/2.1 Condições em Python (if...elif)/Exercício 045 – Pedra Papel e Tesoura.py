# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
j = str(input('Digite uma opção (Pedra, papel ou tesoura): ')).upper().strip()
s = ['PEDRA', 'PAPEL', 'TESOURA']
c = randint (0,2)
print ('-='*40)
print (f'O jogador escolheu {j}, enquanto o computador escolheu {s[c]}.')
print ('-='*40)
if j != s[c]:
    if j == 'PEDRA' and s[c] == 'TESOURA':
        print ('Jogador venceu.')
        print('-=' * 40)
    elif j == 'PEDRA' and s[c] == 'PAPEL':
        print ('Computador venceu.')
        print('-=' * 40)
    elif j == 'PAPEL' and s[c] == 'TESOURA':
        print ('Computador venceu.')
        print('-=' * 40)
    elif j == 'PAPEL' and s[c] == 'PEDRA':
        print ('Jogador venceu.')
        print('-=' * 40)
    elif j == 'TESOURA' and s[c] == 'PEDRA':
        print ('Computador venceu.')
        print('-=' * 40)
    elif j == 'TESOURA' and s[c] == 'PAPEL':
        print ('Jogador venceu.')
        print('-=' * 40)
else:
    print ('EMPATE.')
    print('-=' * 40)
