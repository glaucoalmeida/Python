# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite o salário do funcionário:R$ '))
if s > 1250:
    print (f'O novo salário do funcionário será R${s*(1+0.10):.2f}.')
else:
    print(f'O novo salário do funcionário será R${s*(1+0.15):.2f}.')
