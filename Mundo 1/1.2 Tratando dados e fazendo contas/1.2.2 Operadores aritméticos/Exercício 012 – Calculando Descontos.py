# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do produto? R$ '))
d = p*(1-0.05)
print(f'O novo preço do produto será de R${d:.2f}.')
