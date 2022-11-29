# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print('-=' * 20)
    print(f'Sua média foi {m:.1f}.')
    print ('APROVADO.')
    print('-=' * 20)
elif m >= 5 and m < 7:
    print('-=' * 20)
    print(f'Sua média foi {m:.1f}.')
    print ('RECUPERAÇÃO.')
    print('-=' * 20)
else:
    print('-=' * 20)
    print(f'Sua média foi {m:.1f}.')
    print ('REPROVADO.')
    print('-=' * 20)
