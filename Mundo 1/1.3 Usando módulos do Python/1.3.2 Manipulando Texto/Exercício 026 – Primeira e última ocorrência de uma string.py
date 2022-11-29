# Faça um programa que leia uma frase pelo teclado e mostre:

# - Quantas vezes aparece a letra “A”;
# - Em que posição ela aparece a primeira vez;
# - Em que posição ela aparece a última vez.

f = str(input(('Digite uma frase: ')).strip().upper())
a = f.count('A')
b = f.find('A')+1
c = f.rfind('A')+1
print(f'A letra A aparece {a} vezes.')
print(f'A primeira letra A aparece na posição {b}.')
print(f'A última letra A aparece na posição {c}.')
