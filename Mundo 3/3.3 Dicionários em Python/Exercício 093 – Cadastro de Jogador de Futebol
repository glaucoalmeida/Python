# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

d = {}
l = []
d['nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {d["nome"]} fez? '))
for c in range (0,p):
    l.append(int(input(f'Quantos gols na partida {c+1}? ')))
    d['gols'] = l[:]
    d['total'] = sum(l)
print (d)
for v,k in d.items():
    print (f'{v} = {k}')
print (f'O jogador {d["nome"]} fez {sum(l)} gols.')
for i,v in enumerate(l):
    print (f' => Na {i+1}ª partida fez {v} gols.')
