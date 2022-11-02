num = int(input('Insira um ano:'))
if ((num % 4) == 0) and ((num % 100) != 0):
    print("è um ano bissexto")
else:
    print('não é um ano bissexto')
