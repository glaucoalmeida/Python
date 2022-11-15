# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().

# - A primeira função vai sortear 5 números e vai colocá-los dentro da lista;
# - A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
números = list()
def sorteia(l):
    print ('Os números sorteados foram:',end=' ')
    for c in range (0,5):
        n = randint(1,10)
        números.append(n)
        print (f'{n}',end=' ')
    print ()


def somaPar(l):
    s = 0
    for c in l:
        if c % 2 == 0:
            s += c
    print (f'A soma entre os valores pares sorteados é {s}.')

sorteia(números)
somaPar(números)
