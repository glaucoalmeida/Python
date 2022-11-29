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