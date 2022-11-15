def leiaint (msg):
    while True:
        try:
            a = int(input(msg))
        except (TypeError,ValueError):
            print ('Valor inválido.')
        except KeyboardInterrupt:
            print ('\nO usuário optou por não digitar o número.')
            return 0
        else:
            return int(a)
            break


def leiafloat (msg):
    while True:
        try:
            a = float(input(msg).replace(',','.'))
        except (TypeError,ValueError):
            print ('Valor inválido.')
        except KeyboardInterrupt:
            print ('\nO usuário optou por não digitar o número.')
            return 0
        else:
            return float(a)
            break