nome = str(input('Digite seu nome de usuário:'))
senha = str(input('Digite sua senha:'))
while nome == senha:
    print('Dados inválidos!')
    senha = str(input('Digite sua senha:'))
print('Senha e Nome válidos')
