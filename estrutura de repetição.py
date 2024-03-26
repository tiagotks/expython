'estruturas de repetição (comandos de repetição)'



while True:
 nota = float(input('informe a nota do aluno'))
 if 0 < nota <= 10:
     print ('nota valida!')
     break
 else:
     print('nota invalida!')
