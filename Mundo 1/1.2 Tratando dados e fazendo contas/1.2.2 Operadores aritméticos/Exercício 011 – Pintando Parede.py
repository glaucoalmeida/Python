# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# obs: Admita que cada litro de tinta pinta uma área de 2 metros quadrados.

h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
print(f'A área da parede é de {h*l:.2f}m².')
print(f'Você vai precisar de {(h*l)/2:.2f}L de tinta.')
