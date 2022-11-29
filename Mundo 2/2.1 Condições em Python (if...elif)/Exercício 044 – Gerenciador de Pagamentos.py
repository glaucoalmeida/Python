# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

p = float(input('Digite o preço do produto: R$ '))
print ('-='*20)
print ('Escolha a condição de pagamento: ')
print ('-='*20)
print ('[1] À vista dinheiro/cheque.')
print ('[2] À vista no cartão.')
print ('[3] Em até 2x no cartão.')
print ('[4] 3x ou mais no cartão.')
print ('-='*20)
o = int(input('Qual a opção escolhida? '))
if o == 1:
    print('-=' * 20)
    print (f'O valor a ser pago será de R$ {p * (1-0.1):.2f}.')
    print('-=' * 20)
elif o == 2:
    print('-=' * 20)
    print (f'O valor a ser pago será de R$ {p * (1-0.05):.2f}.')
    print('-=' * 20)
elif o == 3:
    print('-=' * 20)
    print (f'O valor a ser pago será R$ {p:.2f}.')
    print (f'Serão 2 parcelas de R$ {p/2:.2f}.')
    print('-=' * 20)
elif o == 4:
    print('-=' * 20)
    q = int(input('Quantas vezes no cartâo?'))
    print(f'Serão {q} parcelas de R$ {p * (1+0.2)/q:.2f}.')
    print('-=' * 20)
else:
    print('-=' * 20)
    print('Opção inválida. Tente novamente.')
    print('-=' * 20)
