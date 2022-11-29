# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

d = {}
d['Nome'] = str(input('Nome: '))
d['Média'] = float(input('Média: '))
if d['Média'] >= 7:
    d['Situação'] = 'APROVADO'
elif 5 <= d['Média'] < 7:
    d['Situação'] = 'RECUPERAÇÃO'
else:
    d['Situação'] = 'REPROVADO'
for k,v in d.items():
    print (f'{k}: {v}')
