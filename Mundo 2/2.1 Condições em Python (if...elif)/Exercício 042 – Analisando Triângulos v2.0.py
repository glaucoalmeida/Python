# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais;
# – ISÓSCELES: dois lados iguais, um diferente;
# – ESCALENO: todos os lados diferentes.

n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print('-=' * 40)
    print ('Os segmentos podem formar triângulos.')
    if n1 == n2 == n3:
        print ('O triângulo formado é equilátero.')
        print('-=' * 40)
    elif n1 != n2 != n3:
        print ('O triângulo formado é escaleno.')
        print('-=' * 40)
    else:
        print ('O triângulo formado é isósceles.')
        print('-=' * 40)
else:
    print('-=' * 40)
    print('Os segmentos não podem formar triângulos.')
    print('-=' * 40)
