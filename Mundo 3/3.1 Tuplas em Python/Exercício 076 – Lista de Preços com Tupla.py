# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

p = ('Arroz','3.99',
     'Feijão','5.75',
     'Macarrão','2.89',
     'Café','11.99',
     'Leite','7.89')
print ('-'*35)
print ('LISTAGEM DE PREÇOS'.center(35))
print ('-'*35)
for c in range (0,len(p)):
    if c % 2 == 0:
        print (f'{p[c]:.<25}',end='')
    else:
        print(f' R${p[c]:>7}')
print ('-'*35)
