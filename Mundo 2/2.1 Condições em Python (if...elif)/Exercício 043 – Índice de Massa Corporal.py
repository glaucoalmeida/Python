# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC).
# Mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

p = float(input('Digite o peso (kg): '))
h = float(input('Digite a altura (m): '))
IMC = (p/h**2)
if IMC < 18.5:
    print('-=' * 20)
    print (f'Seu IMC é {IMC:.1f}')
    print ('Você está abaixo do peso.')
    print('-=' * 20)
elif IMC >= 18.5 and IMC < 25:
    print('-=' * 20)
    print(f'Seu IMC é {IMC:.1f}')
    print ('Você está no peso ideal.')
    print('-=' * 20)
elif IMC >= 25 and IMC < 30:
    print('-=' * 20)
    print(f'Seu IMC é {IMC:.1f}')
    print ('Você está com sobrepeso.')
    print('-=' * 20)
elif IMC >= 30 and IMC <= 40:
    print('-=' * 20)
    print(f'Seu IMC é {IMC:.1f}')
    print ('Você está obeso.')
    print('-=' * 20)
else:
    print('-=' * 20)
    print(f'Seu IMC é {IMC:.1f}')
    print ('Você está com obesidade mórbida.')
    print('-=' * 20)
