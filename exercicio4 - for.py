# Exibir a tabuada com o número que o usuário inserir

numero = int(input('Insira um número:'))
for n in range(0,11):
    resul = numero * n
    print(numero, 'x', n, '=', resul)