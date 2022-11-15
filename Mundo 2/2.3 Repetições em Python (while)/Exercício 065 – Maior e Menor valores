# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

c = ''
s = a = maior = menor = d = 0
print ('-='*40)
while c in 'S':
    a += 1
    n = int(input('Digite um número: '))
    s += n
    c = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
    print('-=' * 40)
    if a == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
m = s/a
print ('-='*40)
print (f'A média entre os {a} valores digitados foi de {m:.1f}.')
print (f'O maior valor digitado foi {maior}.')
print (f'O menor valor digitado foi {menor}.')
print ('-='*40)
