# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from ex108 import moeda

n = float(input('Digite o valor: R$ '))
print (f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print (f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')
print (f'Aumentando 10%, tem-se: {moeda.moeda(moeda.aumentar(n,10))}.')
print (f'Diminuindo 20%, tem-se: {moeda.moeda(moeda.diminuir(n,20))}.')
