# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

l = []
while True:
    n = int (input('Digite um número: '))
    if n not in l:
        l.append(n)
    else:
        print ('Número já adicionado.')
    z = str(input('Você quer continuar [S/N]?')).upper().strip()[0]
    while z not in 'SN':
        z = str(input('Você quer continuar [S/N]?')).upper().strip()[0]
    if z == 'N':
        break
l.sort()
print (f'Os números digitados foram: {l}')
