# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1   
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador (i,f,p):
    if p < 0:
         p *= -1
    elif p == 0:
         p = 1
    if i < f:
        for c in range (i,f+1,p):
            print (f'{c} ->',end=' ')
        print ('FIM')
    elif i > f:
        for c in range (i,f-1,-p):
            print (f'{c} ->',end=' ')
        print ('FIM')


contador(1,10,1)
contador(10,0,2)
print ('Agora é a sua hora de personalizar a contagem.')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i,f,p)
