# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
d = {}
d['Nome'] = str(input('Nome: '))
a = date.today().year
an = int(input('Ano de nascimento: '))
d['Idade'] = a - an
d['CTPS'] = int(input('CTPS: '))
if d['CTPS'] != 0:
    d['Ano de contratação'] = int(input('Ano de contratação: '))
    d['Salário'] = float(input('Salário: R$ '))
    d['Aposentadoria'] = (d['Ano de contratação'] + 35) - a + d['Idade']
for k,v in d.items():
    print (f'{k}: {v}')
