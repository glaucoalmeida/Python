# Vamos criar um menu em Python, usando modularização.

def leiaint (msg):
    while True:
        try:
            a = int(input(msg))
        except (TypeError,ValueError):
            print ('Valor inválido.')
        except KeyboardInterrupt:
            print ('\nO usuário optou por não digitar o número.')
            return 0
        else:
            return int(a)
            break


def linha (tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print (txt.center(40))
    print(linha())


def menu (l):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in l:
        print (f'{c} - {i}')
        c += 1
    print(linha())
    o = leiaint('Qual sua opção? ')
    return o