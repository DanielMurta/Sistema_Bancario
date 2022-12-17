from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca
from telas import *
import criar_conta

tela_login()
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    agencia = f'{values["agencia"]}-{values["agencia2"]}'
    senha = int(values['senha'])
    if agencia != '' and senha != '':
        if event == 'Login':
            log = criar_conta.login(agencia, senha)
            if log:
                cl = Cliente.Cliente(log[2], log[3], log[4], log[1], log[1])
                ct = ContaPoupanca(agencia, senha, cl, saldo=0)
                tela_principal(cl, ct)
                while True:
                    window, event, values = sg.read_all_windows()
                    if event == sg.WIN_CLOSED:
                        break
    else:
        sg.Popup('Preencha todos os campos!', title='Erro')


    if event == 'Criar conta':
        window.close()
        tela_criar_conta()
        while True:
            window, event, values = sg.read_all_windows()
            if event == sg.WIN_CLOSED:
                exit()
            if event == 'Cancelar':
                window.close()
                tela_login()
                break
            nome = values['nome']
            sobrenome = values['sobrenome']
            cpf = values['sobrenome']
            senha = values['senha']
            repeticao_senha = values['repeticao_senha']
            if senha != '' and repeticao_senha != '':
                if senha == repeticao_senha and event == 'Criar Conta':
                    criar_conta.criar_conta(nome, sobrenome, cpf, senha, repeticao_senha)
                    sg.Popup('Conta criada com sucesso!', font='arial 13', title='Erro')
                    window['nome'].update('')
                    window['sobrenome'].update('')
                    window['cpf'].update('')
                    window['senha'].update('')
                    window['repeticao_senha'].update('')
                else:
                    sg.Popup('As senhas precisam ser iguais!', title='Erro')
            elif nome == '' or sobrenome == '' or cpf == '' or senha == '' or repeticao_senha == '':
                sg.Popup('Verifique se todos os campos estão preenchidos.', title='Erro')










