# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

cor = ('\033[m',
       '\033[0;30;41m',
       '\033[0;30;42m',
       '\033[0;30;43m',
       '\033[0;30;44m',
       '\033[0;30;45m'
       )


def ajuda(comando):
    linha(f'Acessando o comando {comando}...',3)
    print(cor[4], end='')
    help(comando)
    print(cor[0], end='')


def linha(txt, c=0):
    tam = len(txt) + 4
    print(cor[c], end='')
    print('-' * tam)
    print (f'  {txt}')
    print('-' * tam)
    print (cor[0],end='')


while True:
    linha('Bem-vindo a central de ajuda do Python', 2)
    print(cor[5], end='')
    comando = str(input('Função ou biblioteca: '))
    print(cor[0], end='')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda (comando)
linha('Programa finalizado. Até a próxima.',1)
