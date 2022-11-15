#  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas
# – A maior nota   
# – A menor nota
# – A média da turma
# – A situação (opcional)

d = {}
def notas(*num,sit=False):
    d['quantidade de notas'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['média'] = sum(num)/len(num)
    if sit:
        if d['média'] >= 7:
            d['situação'] =  'APROVADO'
        elif 5 <= d['média'] < 7:
            d['situação'] = 'RECUPERAÇÃO'
        else:
            d['situação'] = 'REPROVADO'
    return d

print (notas (8,9,9,7,sit=True))
