# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
a = int(input('Digite o ano (Coloque 0 para analisar o ano atual): '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print(f'O ano de {a} é bissexto.')
else:
    print(f'O ano de {a} não é bissexto.')
