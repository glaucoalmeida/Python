# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

c = str(input('Digite o seu nome completo: ')).strip().upper()
a = 'SILVA' in c
print (f'Seu nome tem Silva? {a}.')
