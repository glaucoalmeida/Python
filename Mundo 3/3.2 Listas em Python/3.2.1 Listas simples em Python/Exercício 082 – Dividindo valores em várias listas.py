# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

l = []
p = []
i = []
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    z = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    while z not in 'SN':
        z = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if z == 'N':
        break
l.sort()
print (f'Os números digitados foram {l}.')
for j,v in enumerate (l):
    if v % 2 == 0:
        p.append(v)
    else:
        i.append(v)
print (f'Os números pares digitados foram {p}.')
print (f'Os números ímpares digitados foram {i}.')
