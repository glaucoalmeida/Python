# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a calcular;
# O segundo chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial (n,show=False):
    f = 1
    for c in range (n,0,-1):
        if show:
            print (f'{c}',end=' ')
            print ('x' if c > 1 else '=',end=' ')
        f *= c
    return f


print (fatorial(6,False))
