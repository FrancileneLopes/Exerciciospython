c = int(input('Quantos graus está fazendo hoje?  '))
f = (9 * c + 160) / 5
if (f >= 45) and (f <= 90):
    print('Temperatura ideal para o experimento')
else:
    print('Temperatura inapropriada para o experimento')
