# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

l = []
for c in range (0,5):
    n = int(input(f'Digite o {c+1}° número: '))
    if c == 0 or n > l[-1]:
        l.append(n)
        print ('Número adicionado ao final da lista.')
    else:
        p = 0
        while p <= len(l):
            if n <= l[p]:
                l.insert(p,n)
                print (f'Número adicionado na posição {p+1}.')
                break
            p += 1
print (f'Os números ordenados: {l}')
