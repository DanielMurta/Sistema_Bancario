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




def login(agencia, senha):
    with open(f'{agencia}.txt', 'r') as arq:
        mensagem = arq.readlines()
        if int(mensagem[1]) == senha:
            with open(f'{agencia}.txt', 'r') as arquivo:
                mensagem = arquivo.readlines()
            return mensagem
        else:
            sg.popup('Senha ou Agência inválidos!')
            return False




