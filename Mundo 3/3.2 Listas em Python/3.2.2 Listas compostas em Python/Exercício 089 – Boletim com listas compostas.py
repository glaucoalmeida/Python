# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

l = []
while True:
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1+n2)/2
    l.append([n,[n1,n2],m])
    z = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    while z not in 'SN':
        z = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if z == 'N':
        break
print (f'{"Nº":<4}{"Nome":<10}{"Média":>9}')
for i,v in enumerate (l):
    print (f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
while True:
    o = int(input('De qual aluno você quer mostrar as notas (999 para parar)? '))
    if o <= len (l) - 1:
        print (f'O aluno {l[o][0]} teve as notas {l[o][1]}.')
    if o == 999:
        break