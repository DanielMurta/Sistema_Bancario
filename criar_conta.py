import random
from Cliente import Cliente
from Conta import Conta
import PySimpleGUI as sg

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
        sg.Popup('ABERTURA DE CONTA COM SUCESSO!'
                 f'\nConta: {mensagem[0]}'
                 f'\nNome: {mensagem[2]}{mensagem[3]}'
                 f'\nFaça LOGIN e comece a usar a conta.', font='arial 13', title='Erro')


def login(agencia, senha):
    try:
        with open(f'{agencia}.txt', 'r') as arq:
            mensagem = arq.readlines()
            if int(mensagem[1]) == int(senha):
                with open(f'{agencia}.txt', 'r') as arquivo:
                    mensagem = arquivo.readlines()
                return mensagem
    except:
        sg.Popup('ERRO AO TENTAR ACESSAR A CONTA!'
                 '\nAgência inválida.', font='arial 13')

    else:
        sg.Popup('SENHA INVÁLIDA!', title='Erro')
        return False






