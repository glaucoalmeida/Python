# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
d = int(input('Qual a quantidade de dias do aluguel? '))
print(f'O preço a ser pago pelo aluguel do carro é de R${60*d+0.15*km:.2f}.')
