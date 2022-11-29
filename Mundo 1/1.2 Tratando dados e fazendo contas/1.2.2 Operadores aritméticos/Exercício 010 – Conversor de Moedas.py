# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Quanto dinheiro você tem na carteira? R$ '))
print(f'Com R${r} você pode comprar US${r/5.20:.2f}.')
