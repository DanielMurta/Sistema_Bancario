from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca
import criar_conta
import PySimpleGUI as sg
from telas import *

sg.theme('DarkRed1')
layout = [[sg.Text("Bem vindo ao Banco Bradisco")],
          [sg.Frame('Login', [[sg.T(s=30)]])]]


window = sg.Window('Caixa Bradisco', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

while True:
    print('[1] LOGIN')
    print('[2] CRIAR CONTA')
    resp = int(input('Opção: '))
    if resp == 1:
        print('-----LOGIN-----')
        agencia = str(input('Agência: '))
        senha = int(input('Senha: '))
        criar_conta.login(agencia, senha)
        with open(f'{agencia}.txt', 'r') as arq:
            mensagem = arq.readlines()
            cl = Cliente(mensagem[2], mensagem[3], mensagem[4], mensagem[1], mensagem[1])
        ct = ContaPoupanca(agencia, senha, cl, saldo=0)
        while True:
            print('[1] Depositar [2] Sacar [3] Saldo [4] Finalizar')
            r = int(input('Opção: '))
            if r == 1:
                deposito = float(input('Valor do depósito: R$ '))
                ct.Depositar(deposito)
            if r == 2:
                saque = float(input('Valor do saque: R$ '))
                ct.sacar(saque)
            if r == 3:
                ct.Informacoes()
            if r == 4:
                break

    if resp == 2:
        criar_conta.criar_conta()






