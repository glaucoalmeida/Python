# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# - a média de idade do grupo;
# - qual é o nome do homem mais velho;
# - quantas mulheres têm menos de 20 anos.

a = b = c = maior = 0
nome = ''
for c in range (1,5):
    n = str(input('Digite o nome: ')).upper().strip()
    i = int(input('Digite a idade: '))
    s = str(input('Digite o sexo [M/F]: ')).upper().strip()
    a += i
    if s == 'F' and i < 20:
         b += 1
    if s == 'M':
        c += i
        if c == 1:
            maior = i
            nome = n
        else:
            if i > maior:
                maior = i
                nome = n
m = a/4
print (f'A média de idade do grupo foi {m:.1f} anos.')
print (f'{nome} é o homem mais velho.')
print (f'{b} mulheres tem menos de 20 anos.')
