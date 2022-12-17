from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca
from telas import *
import criar_conta

tela_login()
while True:
    window, event, values = sg.read_all_windows()
    agencia = f'{values["agencia"]}-{values["agencia2"]}'
    senha = (values['senha'])

    if event == sg.WIN_CLOSED:
        break
    if event == 'Login':
        if agencia == '' or senha == '':
            sg.Popup('Preencha todos os campos!', title='Erro')
        else:
            log = criar_conta.login(agencia, senha)
            if log:
                cl = Cliente.Cliente(log[2], log[3], log[4], log[1], log[1])
                ct = ContaPoupanca(agencia, senha, cl, saldo=0)
                window.close()
                tela_principal(cl, ct)
                while True:
                    window, event, values = sg.read_all_windows()
                    if event == sg.WIN_CLOSED:
                        exit()
                    if event == 'Sair':
                        window.close()
                        tela_login()
                        break
                    if event == 'Exibir Extrato':
                        window['extrato'].update(f'Nome: {cl.nome}'
                                                 f'\nConta: {ct.agencia}'
                                                 f'\nSaldo: R${ct.saldo:.2f}')

                    if event == 'Depositar':
                        window.close()
                        tela_depositar()
                        while True:
                            window, event, values = sg.read_all_windows()
                            valor_deposito = values['valor_deposito']
                            if event == sg.WIN_CLOSED:
                                exit()
                            if event == 'Sair':
                                window.close()
                                tela_principal(cl, ct)
                                break

                            if event == 'Cancelar':
                                window['valor_deposito'].update('')

                            if event == 'Confirmar':
                                if valor_deposito == '':
                                    sg.Popup('Preencha todos os campos!', title='Erro')
                                else:
                                    ct.Depositar(float(valor_deposito))
                                    sg.Popup('DEPÓSITO CONCLUÍDO!')
                                    window['valor_deposito'].update('')

                    if event == '   Sacar   ':
                        window.close()
                        tela_sacar()
                        while True:
                            window, event, values = sg.read_all_windows()
                            valor_saque = values['valor_saque']
                            if event == sg.WIN_CLOSED:
                                exit()
                            if event == 'Sair':
                                window.close()
                                tela_principal(cl, ct)
                                break

                            if event == 'Cancelar':
                                window['valor_saque'].update('')

                            if event == 'Confirmar':
                                if valor_saque == '':
                                    sg.Popup('Preencha todos os campos!', title='Erro')
                                else:
                                    ct.sacar(float(valor_saque))
                                    sg.Popup('SAQUE CONCLUÍDO!'
                                             '\nRetire o Dinheiro')
                                    window['valor_saque'].update('')


            elif not log:
                sg.Popup('Senha ou Agência inválidos!', title='Erro')


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
            cpf = values['cpf']
            senha = values['senha']
            repeticao_senha = values['repeticao_senha']
            if senha != '' and repeticao_senha != '':
                if senha == repeticao_senha and event == 'Criar Conta':
                    criar_conta.criar_conta(nome, sobrenome, cpf, senha, repeticao_senha)
                    window['nome'].update('')
                    window['sobrenome'].update('')
                    window['cpf'].update('')
                    window['senha'].update('')
                    window['repeticao_senha'].update('')
                else:
                    sg.Popup('As senhas precisam ser iguais!', title='Erro')
            elif nome == '' or sobrenome == '' or cpf == '' or senha == '' or repeticao_senha == '':
                sg.Popup('Verifique se todos os campos estão preenchidos.', title='Erro')










