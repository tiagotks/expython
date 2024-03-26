while True:
    login = str(input('Crie o seu login'))
    senha = str(input('crie uma senha'))
    if login == senha:
        print('erro! login e senha nao podem ser iguais')
    else:
        print('login e senha criado com sucesso')
        break