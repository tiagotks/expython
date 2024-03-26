Notas = []

while True:
    nota = int(input('digite uma nota: '))
    if 0 < nota <= 10:
        Notas.append(nota)
    else:
        print('nota invalida!')
        break
    print(notas)
