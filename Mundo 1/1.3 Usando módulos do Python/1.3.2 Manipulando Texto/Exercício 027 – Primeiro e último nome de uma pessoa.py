# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
a = n.split()[0]
b = n.split()[-1]
print (f'Seu primeiro nome é {a}.')
print (f'Seu último nome é {b}.')
