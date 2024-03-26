''' faca um programa que fique pedindo numeros quaisquer e armzena em uma lista chamada numeros.
caso o numero seja maior que 50, o programa é encerrado.'''

Lista = []
while True:
    numero = int(input('digite uma numero: '))
    if 0 < numero35\
            <= 50:
        Lista.append(numero)
    else:
        print('lista encerradaa!')
        break
    print(Lista)