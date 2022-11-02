casa = float(input('Por favor, insira o valor da casa:'))
salario = float(input('Qual o salário do comprador?'))
anos = int(input('Informe em quantos anos você quer pagar:'))
meses = anos * 12
prestacaoMensal = casa/meses
limite: float = (30 * salario) / 100
if prestacaoMensal > limite:
    print('Infelizmente você não pode financiar essa casa!')
else:
    print('A prestação mensal vai ser de: {}!'.format(prestacaoMensal))


