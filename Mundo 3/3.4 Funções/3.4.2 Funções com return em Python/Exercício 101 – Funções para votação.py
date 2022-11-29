# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa;
# Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date
def voto (a):
    i = date.today().year - a
    if 18 <= i <= 65:
        return f'Com {i} anos, o voto é obrigatório.'
    if 16 <= i < 18 or i > 65:
        return f'Com {i} anos, o voto é opcional.'
    else:
        return f'Com {i} anos, não é preciso votar.'


print(voto(2009))
