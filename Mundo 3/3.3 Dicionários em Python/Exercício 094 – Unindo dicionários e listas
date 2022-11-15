# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre:

# A) Quantas pessoas foram cadastradas;
# B) A média de idade;
# C) Uma lista com as mulheres;
# D) Uma lista de pessoas com idade acima da média.

d = {}
l = []
s = 0
while True:
    d['Nome'] = str(input('Nome: '))
    d['Idade'] = int(input('Idade: '))
    s += d['Idade']
    while True:
        d['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if d['Sexo'] not in 'MF':
            print ('Opção inválida. Tente novamente.')
        else:
            break
    l.append(d.copy())
    d.clear()
    z = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if z not in 'SN':
        print('Opção inválida. Tente novamente.')
    elif z == 'N':
        break
m = s/len(l)
print (f'{len(l)} pessoas foram cadastradas.')
print (f'A média de idade dentre as pessoas cadastradas foi de {m:.1f} anos.')
print (f'O nome das mulheres cadastradas são:',end=' ')
for p in l:
    if p['Sexo'] == 'F':
        print (f'[{p["Nome"]}]',end=' ')
print ()
print (f'As pessoas com idade acima da média são:',end=' ')
for p in l:
    if p['Idade'] > m:
        print ('    ',end=' ')
        print()
        for k,v in p.items():
            print (f'{k}: {v};',end=' ')