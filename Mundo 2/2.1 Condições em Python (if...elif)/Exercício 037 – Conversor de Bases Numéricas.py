# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número: '))
print ('-='*15)
print ('Escolha a base de conversão: ')
print ('-='*15)
print ('[1] Binário')
print ('[2] Octal')
print ('[3] Hexadecimal')
print ('-='*15)
i = int(input('Qual a base de conversão? '))
print ('-='*15)
if i == 1:
    print (f'{n} em binário é {bin(n)[2:]}.')
    print('-=' * 15)
elif i == 2:
    print(f'{n} em octal é {oct(n)[2:]}.')
    print('-=' * 15)
elif i == 3:
    print(f'{n} em hexadecimal é {hex(n)[2:]}.')
    print('-=' * 15)
else:
    print ('Opção inválida. Tente novamente.')
    print('-=' * 15)
