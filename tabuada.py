op = int(input('Escolha a operação: [1] Adição, [2] Subtração, [3] Multiplicação, [4] Divisão'))
num = int(input('Digite um número que você queira saber a tabuada:'))
numDois = int(input('Por qual número?'))
if op == 1:
    resultadoAd = num + numDois
    print('O resultado de', num , "+", numDois, "é: ", resultadoAd)
elif op == 2:
    resultadoAd = num - numDois
    print('O resultado de', num , "-", numDois, "é: ", resultadoAd)
elif op == 3:
    resultadoAd = num * numDois
    print('O resultado de', num , "x", numDois, "é: ", resultadoAd)
elif op == 4:
    resultadoAd = num / numDois
    print('O resultado de', num , "/", numDois, "é: ", resultadoAd)



