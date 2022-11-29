# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que aceitando apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print ('Valor inválido.')
    return n


n = leiaint('Digite um número: ')
print (f'O número digitado foi {n}.')
