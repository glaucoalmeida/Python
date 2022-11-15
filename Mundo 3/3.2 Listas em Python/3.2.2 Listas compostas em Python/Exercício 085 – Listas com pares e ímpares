# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.



l = [[], []]
for c in range (0,7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
l[0].sort()
l[1].sort()
print (f'Os números pares digitados foram {l[0]}')
print (f'Os números ímpares digitados foram {l[1]}')
