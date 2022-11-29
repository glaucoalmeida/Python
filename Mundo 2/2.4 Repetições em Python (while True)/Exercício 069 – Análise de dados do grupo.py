# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

a = b = d = 0
while True:
    print('-=' * 20)
    i = int(input('Digite a idade: '))
    if i >= 18:
        a += 1
    s = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while s not in 'MF':
        s = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if s == 'M':
        b += 1
    if s == 'F' and i < 20:
        d += 1
    c = str(input('Você quer continuar [S/N]? '))
    while c not in 'SN':
        c = str(input('Você quer continuar [S/N]? '))
    if c == 'N':
        break
print('-=' * 20)
print (f'{a} pessoas tem mais de 18 anos.')
print (f'{b} homens foram cadastrados.')
print (f'{d} mulheres tem menos de 20 anos.')
print('-=' * 20)
