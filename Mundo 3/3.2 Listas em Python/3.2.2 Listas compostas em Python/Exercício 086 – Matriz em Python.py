# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

m = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        m [l][c] = int(input(f'Digite o número na posição {l}x{c}: '))
for l in range (0,3):
    for c in range (0,3):
        print (f'[{m[l][c]:^3}]',end='')
    print()
