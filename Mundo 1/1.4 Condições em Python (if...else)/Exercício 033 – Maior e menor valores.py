# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
lista = [a,b,c]
print(f'O maior número é {max(lista)}.')
print(f'O menor número é {min(lista)}.')
