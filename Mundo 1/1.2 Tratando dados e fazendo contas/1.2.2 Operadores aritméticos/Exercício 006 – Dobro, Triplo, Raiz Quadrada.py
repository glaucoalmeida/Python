# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt
n = int(input('Digite um número: '))
print(f'O dobro de {n} é {2*n}.')
print(f'O triplo de {n} é {3*n}.')
print(f'A raiz quadrada de {n} é {sqrt(n):.2f}.')
