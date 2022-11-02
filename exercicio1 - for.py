# Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artificios, indo de 10 a 0 com uma pausa de 1 segundo
import time

for contador in range(10, 0, -1):
    time.sleep(1)
    print(contador)
print('Fogos!!!')
