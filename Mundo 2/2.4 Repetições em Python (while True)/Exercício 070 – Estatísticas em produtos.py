# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

a = b = c = menor = 0
d = ''
print('-=' * 20)
while True:
    n = str(input('Digite o nome do produto: ')).upper().strip()
    p = float(input('Digite o preço do produto: R$ '))
    a += p
    if p > 1000:
        b += 1
    if c == 1:
        c += 1
        menor = p
        d = n
    else:
        if p < menor:
            p = menor
            d = n
    v = str(input('Você quer continuar [S/N]? '))
    print('-=' * 20)
    while v not in 'SN':
        v = str(input('Você quer continuar [S/N]? ')).upper().strip()
    if v == 'N':
        break
print('-=' * 20)
print (f'Foram gastos no total R$ {a:.2f}.')
print (f'{b} produtos custam mais de R$ 1000.')
print (f'{n} é o produto mais barato.')
print('-=' * 20)
