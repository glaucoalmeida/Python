# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# se ele ainda vai se alistar ao serviço militar;
# se é a hora exata de se alistar;
# se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
a = int(input('Digite o ano de nascimento: '))
b = date.today().year
i = b - a
if i < 18:
    print('-=' * 30)
    print ('Você ainda irá se alistar.')
    print (f'Faltam {18 - i} anos para o alistamento.')
    print('-=' * 30)
elif i > 18:
    print('-=' * 30)
    print ('Você já deveria ter se alistado.')
    print (f'Você está atrasado {i - 18} anos para o alistamento.')
    print('-=' * 30)
elif i == 18:
    print ('-=' * 30)
    print ('Você deve se alistar imediatamente.')
    print('-=' * 30)
