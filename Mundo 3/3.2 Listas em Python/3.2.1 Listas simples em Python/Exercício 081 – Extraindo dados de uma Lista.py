# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
                                                                                                                          
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

l = []
while True:
    l.append(int(input('Digite um número: ')))
    z = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
    while z not in 'SN':
        z = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
    if z == 'N':
        break
l.sort(reverse=True)
print (f'Foram digitados {len(l)} números.')
print (f'Os valores digitados de forma decrescente: {l}')
if 5 in l:
    print ('O número 5 foi digitado.')
else:
    print ('O número 5 não foi digitado.')
