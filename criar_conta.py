import random
from Cliente import Cliente
from Conta import Conta

def criar_conta(nome, sobrenome, cpf, senha, repeticao_senha):
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
        arq.write(f'{agencia} \n{senha} \n{nome.capitalize()} \n{sobrenome} \n{cpf}')
    with open(f'{agencia}.txt', 'r') as arq:
        mensagem = arq.readlines()
        print('-- Abertura da conta com sucesso! --')
        print(f'Agência: {mensagem[0]}')
        print(f'Nome: {mensagem[2]}')
        print(f'Senha: {mensagem[1]}')
    print('\033[32m[Faça o LOGIN e comece a usar sua conta!]\033[m')


def login(agencia, senha):
    with open(f'{agencia}.txt', 'r') as arq:
        mensagem = arq.readlines()
        if int(mensagem[1]) == senha:
            return print('Acesso concluído!')
        else:
            print('Senha incorreta')




