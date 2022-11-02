idd = int(input('Qual é a sua idade?'))
if idd <= 9:
    print('Você está na categoria: Mirim!')
elif 10 <= idd <= 14:
    print('Você está na categoria: Infantil!')
elif 15 <= idd <= 19:
    print('Você está na categoria: Junior!')
elif idd == 20:
    print('Você está na categoria: Sênior!')
elif idd > 20:
    print('Você está na categoria: Master!')
