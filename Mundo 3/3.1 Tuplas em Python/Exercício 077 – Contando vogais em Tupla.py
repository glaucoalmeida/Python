# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

nomes = ('Alemanha','Argentina','Brasil','Espanha','Inglaterra',
         'Holanda','Itália','França','Uruguai','Portugal')
for n in nomes:
    print (f'\nEm {n}, tem-se:',end=' ')
    for l in n:
        if l.lower() in 'aeiou':
            print (l,end=' ')
