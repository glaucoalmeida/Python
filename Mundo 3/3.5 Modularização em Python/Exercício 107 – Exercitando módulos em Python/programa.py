# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from ex107 import moeda

n = float(input('Digite o valor: R$ '))
print (f'O dobro de {n} é {moeda.dobro(n)}.')
print (f'A metade de {n} é {moeda.metade(n)}.')
print (f'Aumentando 10%, tem-se: {moeda.aumentar(n,10)}.')
print (f'Diminuindo 20%, tem-se: {moeda.diminuir(n,20)}.')
