# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.                                                                                                               
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

l = []
s = []
maior = menor = 0
while True:
    s.append(str(input('Nome: ')))
    s.append(float(input('Peso: ')))
    if len(l) == 0:
        maior = menor = s[1]
    else:
        if s[1] > maior:
            maior = s[1]
        elif s[1] < menor:
            menor = s[1]
    l.append(s[:])
    s.clear()
    z = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if z not in 'SN':
        z = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if z == 'N':
        break
print (f'{len(l[0])} pessoas foram cadastradas.')
print (f'A pessoa mais pesada pesa {maior} kg e se chama:',end=' ')
for v in l:
    if v[1] == maior:
        print (f'[{v[0]}]',end=' ')
print ()
print (f'A pessoa mais leve pesa {menor} kg e se chama:',end=' ')
for v in l:
    if v[1] == menor:
        print (f'[{v[0]}]',end=' ')
