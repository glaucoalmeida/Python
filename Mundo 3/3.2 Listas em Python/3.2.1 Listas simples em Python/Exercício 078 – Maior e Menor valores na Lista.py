# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

l = []
maior = menor = 0
for c in range (0,5):
    l.append(int(input(f'Digite o {c+1}º número: ')))
    if c == 0:
        maior = menor = l[c]
    else:
        if l[c] > maior:
            maior = l[c]
        elif l[c] < menor:
            menor = l[c]
l.sort()
print (f'Os números digitados foram {l}.')
print (f'O maior valor digitado foi {maior} e está na posição:',end=' ')
for i,v in enumerate(l):
    if v == maior:
        print (f'{i+1}',end=' ')
print ()
print (f'O menor valor digitado foi {menor} e está na posição:',end=' ')
for i,v in enumerate(l):
    if v == menor:
        print (f'{i+1}',end=' ')
