# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

s = maior = menor = 0
for c in range (1,6):
    p = float(input('Digite o peso (kg): '))
    s += 1
    if s == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print (f'O maior peso digitado foi {maior}.')
print (f'O menor peso digitado foi {menor}.')
