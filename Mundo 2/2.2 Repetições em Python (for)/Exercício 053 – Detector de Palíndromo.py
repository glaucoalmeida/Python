# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = str(input('Digite uma frase: ')).strip().upper()
a = f.split()
b = ''.join(a)
i = ''
for c in range (len(b)-1,-1,-1):
    i += b[c]
if i == b:
    print ('É palíndromo.')
else:
    print ('Não é palíndromo.')
