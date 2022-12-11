from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca
from telas import *
import criar_conta
import PySimpleGUI as sg

tela_login()
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Login':
        agencia = values['agencia']
        senha = int(values['senha'])
        log = criar_conta.login(agencia, senha)
        if log:
            cl = Cliente(log[2], log[3], log[4], log[1], log[1])
            ct = ContaPoupanca(agencia, senha, cl, saldo=0)
            sg.theme('DarkRed1')
            tela_principal()
            while True:
                window, event, values = sg.read_all_windows()
                if event == sg.WIN_CLOSED:
                    break
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

    if event == 'Criar conta':
        window.close()
        while True:
            window, event, values = sg.read_all_windows()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Cancelar':
                break
            nome = values['nome']
            sobrenome = values['sobrenome']
            cpf = values['sobrenome']
            senha = values['senha']
            repeticao_senha = values['repeticao_senha']
            if event == 'Criar Conta':
                criar_conta.criar_conta(nome, sobrenome, cpf, senha, repeticao_senha)







