idd = int(input('Qual a sua idade?'))
if idd < 18:
    falta = 18 - idd
    print('Você não pode se alistar! Falta {} ano(s) para você poder se alistar'.format(falta))
elif idd == 18:
    print('Está na hora de se alistar!')
elif idd > 18:
    passou = idd - 18
    print('Passou seu tempo de alistamento! Passou do prazo de alistamento {} ano(s)'.format(passou))
