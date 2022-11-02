#Fazer a soma entre todos os números impares que são multiplos
# de 3 e se encontram no intervalo de 1 a 500

for impar in range(0, 500):
    if (impar % 2 ) == 1 and (impar % 3 ) ==0 :
        print(impar)
        