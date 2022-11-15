# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

s1 = s2 = 0
from datetime import date
for c in range (1,8):
    a = int(input('Digite o ano de nascimento: '))
    b = date.today().year
    i = b - a
    if i >= 18:
        s1 += 1
    else:
        s2 += 1
print (f'{s1} pessoas são de maior.')
print (f'{s2} pessoas são de menor.')
