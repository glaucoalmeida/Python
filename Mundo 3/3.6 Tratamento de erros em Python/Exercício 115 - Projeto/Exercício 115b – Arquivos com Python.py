# Vamos ver como fazer acesso a arquivos usando o Python.

from ex115.interface import *

def arqnex(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar (nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um problema na criação do arquivo')
    else:
        print (f'O arquivo {nome} foi criado com sucesso.')


def lerarq(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Não foi possível ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1]=dado[1].replace('\n','')
            print (f'{dado[0]:<30}{dado[1]:>5} anos')


def cad(arq,n='desconhecido',i=0):
    try:
        a = open(arq,'at')
    except:
        print ('Houve uma problema na adição do cadastro.')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print ('Houve um problema no salvamento do cadastro.')
        else:
            print (f'{n} foi adicionado com sucesso.')