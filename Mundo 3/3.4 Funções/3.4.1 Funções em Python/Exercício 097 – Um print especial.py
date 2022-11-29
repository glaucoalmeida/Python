# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem em tamanho adaptável.
#Ex:                                                                                                                                                                escreva(‘Olá, Mundo!’) Saída:                                                                                                                          ~~~~~~~~~                                                                                                                                                           Olá,Mundo!                                                                                                                                                          ~~~~~~~~~      


def escreva (txt):
    tam = len(txt) + 4
    print ('-'*tam)
    print (f'  {txt}')
    print('-' * tam)


escreva ('Olá, mundo.')
escreva('Eu amo programar.')
