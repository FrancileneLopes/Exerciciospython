a = float(input('Insira o primeiro valor:    '))
b = float(input('Insira o segundo valor:    '))
c = float(input('Insira o terceiro valor:    '))
#ABC
if a < b and b < c :
    print('A ordem é', a, b, c)
if a < c and c < b :
    print('A ordem é', a, c, b)
#BAC
if b < a and a < c :
    print('A ordem é', b, a, c)
#BCA
if b < c and c < a :
    print('A ordem é', b, c, a)
#CAB
if c < a and a < b :
    print('A ordem é', c, a, b)
#CBA
if c < b and b < a :
    print('A ordem é', c, b, a)
