# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
l = []
s = []
q = int(input('Quantos jogos você quer gerar? '))
t = 1
while t <= q:
    c = 0
    while True:
        n = randint(1,60)
        if n not in l:
            l.append(n)
            c += 1
        if c == 6:
            break
    l.sort()
    s.append(l[:])
    l.clear()
    t += 1
for i,v in enumerate(s):
    print (f'Jogo {i+1}: {v}')
    sleep(1)
