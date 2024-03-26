salario_atual = float(input('informe o seu salario atual'))
if salario_atual < 2000:
    print('Salario Atual: ', salario_atual)
    print('so seu salario recebera um aumento de 20%')
    novo_salario = salario_atual*1.20
    valor_do_aumento_real = novo_salario - salario_atual
    print('valor do aumento em R$: ', valor_do_aumento_real)
    print('o seu novo salario e R$', novo_salario)
elif 2000 <= salario_atual < 3500:
    print('o seu novo salario recebera um aumento de 15%')
    novo_salario = salario_atual*1.15
    valor_do_aumento_real = novo_salario - salario_atual
    print('valor do aumento em R$: ', valor_do_aumento_real)
    print('o seu novo salario e R$', novo_salario)
elif 3500 <= salario_atual < 5000:
    print('o seu novo salario recebera um aumento de 10%')
    novo_salario = salario_atual*1.10
    valor_do_aumento_real = novo_salario - salario_atual
    print('valor do aumento em R$: ', valor_do_aumento_real)
    print('o seu novo salario e R$', novo_salario)
else:
    print('salario atual: ', salario_atual)
    print('o seu salario recebara um aumento 10%')
    novo_salario = salario_atual*1.05
    valor_do_aumento_real = novo_salario - salario_atual
    print('valor do aumento em R$: ', valor_do_aumento_real)
    print('o seu novo salario e R$', novo_salario)
