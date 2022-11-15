# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print ('-='*40)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print ('-='*40)
while True:
    print ('Escolha uma das opções.')
    print('-=' * 40)
    print ('[1] Somar')
    print ('[2] Multiplicar')
    print ('[3] Maior')
    print ('[4] Novos números')
    print ('[5] Fim do programa')
    print('-=' * 40)
    o = int(input('Qual a opção escolhida? '))
    print('-=' * 40)
    if o == 1:
        print (f'{n1} + {n2} = {n1 + n2}.')
        print('-=' * 40)
    elif o == 2:
        print (f'{n1} x {n2} = {n1 * n2}.')
        print('-=' * 40)
    elif o == 3:
        if n1 > n2:
         print (f'{n1} é maior que {n2}.')
         print('-=' * 40)
        elif n2 > n1:
         print (f'{n2} é maior que {n1}.')
         print('-=' * 40)
        else:
            print(f'{n1} é igual a {n2}.')
            print('-=' * 40)
    elif o == 4:
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite outro número:'))
        print('-=' * 40)
    elif o == 5:
        break
    else:
     print ('Opção inválida. Tente novamente.')
     print('-=' * 40)
print ('Programa encerrado.')
print ('-='*40)