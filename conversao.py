num = int(input('Digite o número que você quer converter'))
escolha = int(input('Digite o número para a conversão: [1] Binário, [2]Octal, [3] Hexadecimal'))
Cbin = format(num, 'b')
if escolha == 1:
    print('O número ', num, 'convertido para Binário é ', Cbin)
elif escolha == 2:
    octal = oct(num)
    print('O número, ', num, 'convertido para Octal é: ', octal )
else:
    hexa = hex(num)
    print('O número ', num, 'convertido para Hexadecimal é ',hexa )

