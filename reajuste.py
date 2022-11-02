salario = float(input('Qual o seu salário atual?'))
novoSalario = ((3 * salario) / 100) + salario
if salario <= 1050 :
    print('Seu novo salario é: ', novoSalario + 200)
else:
    print('Seu novo salario é: ', novoSalario)
