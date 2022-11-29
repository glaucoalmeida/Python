# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

d = {}
l = []

d['Jogador 1'] = randint(1,6)
d['Jogador 2'] = randint(1,6)
d['Jogador 3'] = randint(1,6)
d['Jogador 4'] = randint(1,6)
for i,k in d.items():
    print (f'{i} jogou {k}.')
    sleep (1)
l = sorted(d.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate (l):
    print (f'{i+1}ª posição: {v[0]} com {v[1]}.')
    sleep(1)
