# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

s = 0
from random import randint
c = randint (0,10)
while True:
    j = int(input('Digite um número: '))
    s += 1
    if j == c:
        break
print ('-='*40)
print (f'O número escolhido pelo computador foi {c}.')
print (f'Foram necessárias {s} tentativas para o jogador vencer.')
print ('-='*40)
