# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Fortaleza.

times = ('Palmeiras','Internacional','Flamengo','Fluminense','Corinthians',
         'Athletico','Atlético MG','São Paulo','América MG','Fortaleza',
         'Botafogo','Santos','Bragantino','Goiás','Coritiba',
         'Cuiabá','Ceará','Atlético GO','Avaí','Juventude')

print (f'Os 5 primeiros colocados são {times[0:5]}.')
print (f'Os 4 últimos colocados são {times[16:21]}.')
print (f'Os times em ordem alfabética: {sorted(times)}.')
print (f'O Fortaleza está na {times.index("Fortaleza")+1}ª posição.')
