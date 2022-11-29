# Aprimore o desafio anterior, mostrando no final:      
                                              
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                               
# C) O maior valor da segunda linha.

m = [[0,0,0],[0,0,0],[0,0,0]]
sp = sc = maior = 0
for l in range (0,3):
    for c in range (0,3):
        m[l][c] = int(input(f'Digite o número na posição {l}x{c}: '))
for l in range (0,3):
    for c in range (0,3):
        print (f'[{m[l][c]:^5}]',end='')
        if m[l][c] % 2 == 0:
            sp += m[l][c]
    print()
print (f'A soma dos valores pares é {sp}.')
print (f'A soma dos valores da terceira coluna é',end=' ')
for l in range (0,3):
    sc += m[l][2]
print (f'{sc}.',end=' ')
print ()
print ('O maior valor da segunda linha é',end=' ')
for c in range (0,3):
    if c == 0:
        maior = m[1][c]
    else:
        if m[1][c] > c:
            maior = m[1][c]
print (f'{maior}.',end=' ')
