# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área (l,c):
    a = l*c
    print (f'O terreno com dimensões {l} m x {c} m tem uma área de {a:.2f} m².')


l = float(input('Qual a largura (m)? '))
c = float(input('Qual o comprimento (m)? '))
área (l,c)
