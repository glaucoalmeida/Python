# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = ' '
while s not in 'MF':
    s = str(input('Digite o sexo [M/F]: ')).strip().upper()
