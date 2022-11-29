# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

d = {}
l = []
s = []
while True:
    d.clear()
    d['nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas {d["nome"]} fez? '))
    for c in range (0,p):
        l.append(int(input(f'Quantos gols na partida {c+1}? ')))
        d['gols'] = l[:]
        d['total'] = sum(l)
    s.append(d.copy())
    l.clear()
    z = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
    while z not in 'SN':
        print ('Opção inválida. Tente novamente.')
        z = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
    if z == 'N':
        break
print ('cod ',end='')
for i in d.keys():
    print (f'{i:<15} ',end='')
print ()
for i,v in enumerate (s):
    print (f'{i:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print ()
while True:
    q = int(input('De qual jogador você quer mostrar os dados (999 para parar)? '))
    if q <= len(s) - 1:
        print (f'Levantamento de dados do jogador {s[q]["nome"]}.')
        for i,v in enumerate (s[q]["gols"]):
            print (f'Na partida {i+1}, ele fez {v} gols.')
    elif q == 999:
        break
    else:
        print ('Jogador não encontrado.')