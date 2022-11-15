# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5.
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

num = int(input('Tente adivinhar um número entre 0 e 5: '))
computador = randint (0,5)
print (f'O número que você escolheu foi {num}.')
print ('CARREGANDO')
sleep(1)
print (f'O número que eu escolhi foi {computador}.')
if num == computador:
    print ('Parabéns, você conseguiu ganhar!')
else:
    print ('Que pena, você errou!')
