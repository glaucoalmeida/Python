# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = (int(input('Digite o 1° número: ')),
    int(input('Digite o 2° número: ')),
    int(input('Digite o 3° número: ')),
    int(input('Digite o 4° número: ')))
print (f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print (f'O número 3 apareceu na {n.index(3)}ª posição.')
else:
    print ('O número 3 não foi digitado.')
print ('Os números pares foram:',end=' ')
for c in n:
    if c % 2 == 0:
        print (c,end=' ')
