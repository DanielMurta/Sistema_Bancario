import random

def criar_conta():
    nome = str(input('Nome: '))
    sobrenome = str(input('Sobrenome: '))
    cpf = str(input('CPF: '))
    senha = str(input('Senha (6 digitos): '))
    repeticao_senha = str(input('Digite a senha novamente: '))
    while True:
        if repeticao_senha == senha:
            break
        else:
            print('As senhas precisam ser iguais')
            repeticao_senha = str(input('Digite a senha novamente: '))
    num = random.randint(1000, 9999)
    dig = random.randint(1, 9)
    agencia = f'{num}-{dig}'
    saldo = 0
    with open(f'{agencia}.txt', 'w') as arq:
        arq.write(f'Agência: {agencia} \n{senha} \nNome: {nome.capitalize()} \nSobrenome: {sobrenome} '
                  f'\nCPF: {cpf} \nSaldo: {saldo}')
    with open(f'{agencia}.txt', 'r') as arq:
        mensagem = arq.readlines()
        print(mensagem[0])
        print(mensagem[2])
        print(mensagem[1])
    print('\033[32m[Cadastro Concluído]\033[m')


def login(agencia, senha):
    with open(f'{agencia}.txt', 'r') as arq:
        mensagem = arq.readlines()
        if int(mensagem[1]) == senha:
            print('Acesso concluído!')
        else:
            print('Senha incorreta')




