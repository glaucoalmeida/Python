# Vamos finalizar o projeto de acesso a arquivos em Python.

from ex115.interface import *
from ex115.arquivo import *

arq = 'programa.txt'
if not arqnex(arq):
    criar(arq)

while True:
    r = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if r == 1:
        lerarq(arq)
    elif r == 2:
        cabeçalho('NOVO CADASTRO')
        n = str(input('Nome: '))
        i = int(input('Idade: '))
        cad(arq,n,i)
    elif r == 3:
        break
    else:
        print('Opção inválida.')
print (linha())
print ('Programa finalizado.')
print (linha())
