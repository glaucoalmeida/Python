def aumentar (n=0,x=0,f=False):
    r = n*(1+(x/100))
    return r if f is False else moeda(r)


def diminuir (n=0,x=0,f=False):
    r = n*(1-(x/100))
    return r if f is False else moeda(r)


def dobro (n=0,f=False):
    r = 2*n
    return r if f is False else moeda(r)


def metade (n=0,f=False):
    r = n/2
    return r if f is False else moeda(r)


def moeda(n=0,p='R$ '):
    return f'{p}{n:.2f}'.replace('.',',')


def resumo(n,a=0,d=0):
    print ('-'*35)
    print ('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print (f'O valor analisado é {moeda(n)}.')
    print(f'O dobro é {(moeda(dobro(n)))}.')
    print (f'A metade é {(moeda(metade(n)))}')
    print (f'Aumentando {a}%, tem-se {moeda(aumentar(n,a))}.')
    print(f'Diminuindo {d}%, tem-se {moeda(diminuir(n,d))}.')
    print('-' * 35)