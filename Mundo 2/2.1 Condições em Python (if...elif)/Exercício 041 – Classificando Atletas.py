# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
a = int(input('Digite o ano de nascimento: '))
b = date.today().year
i = b - a
if i <= 9:
    print ('MIRIM.')
elif i > 9 and i <= 14:
    print ('INFANTIL.')
elif i > 14 and i <= 19:
    print ('JÚNIOR.')
elif i > 19 and i <= 25:
    print ('SÊNIOR.')
else:
    print ('MASTER.')
