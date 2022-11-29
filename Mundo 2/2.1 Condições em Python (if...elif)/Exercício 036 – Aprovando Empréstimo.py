# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print ('-='*20)
v = float(input('Digite o valor da casa: R$ '))
s = float(input('Digite o salário do comprador: R$ '))
a = int(input('Quantos anos de pagamento? '))
p = v/(a * 12)
if p > s * 0.3:
    print('-=' * 40)
    print ('O empréstimo será negado.')
    print (f'As parcelas seriam de R$ {p:.2f}, enquanto o comprador só pode pagar R$ {s * 0.3:.2f}.')
    print('-=' * 40)
else:
    print ('-='* 40)
    print('O empréstimo será aceito.')
    print(f'As parcelas serão de R$ {p:.2f} por mês durante {a} anos.')
    print('-=' * 40)
