# Importando classe Cliente
from Cliente import Cliente
# Importando classe Conta
from Conta import ContaPoupanca
# Importando Telas
from telas import *
# Importando função para login e criação de conta
import criar_conta

# Chamando tela login
tela_login()
while True:
    window, event, values = sg.read_all_windows()
    # Armazenando os dados dos campos nas variávels agencia e senha
    agencia = f'{values["agencia"]}-{values["agencia2"]}'
    senha = (values['senha'])

    # Fechar a tela
    if event == sg.WIN_CLOSED:
        break
    # Fazendo Login
    if event == 'Login':
        # Implementando exceções (Todos os campos devem ser preenchidos)
        if agencia == '' or senha == '':
            # Mensagem de ERRO
            sg.Popup('Preencha todos os campos!', title='Erro')
        else:
            # Armazenando os dados do cliente na variável log.
            log = criar_conta.login(agencia, senha)
            # Se o log não retornar Falso
            if log:
                # Chamando as funções Cliente e ContaPoupança com os parãmetros dos dados do cliente na variável log
                cl = Cliente(log[2], log[3], log[4], log[1], log[1])
                ct = ContaPoupanca(agencia, senha, cl, saldo=0)  # Definindo saldo como padrão = 0
                # Fechando tela login
                window.close()
                # Abrindo tela Principal
                tela_principal(cl, ct)
                while True:
                    window, event, values = sg.read_all_windows()
                    if event == sg.WIN_CLOSED:
                        exit()
                    # Saindo da tela Principal e voltando para a tela login
                    if event == 'Sair':
                        window.close()
                        tela_login()
                        break
                    # Exibindo Extrato
                    if event == 'Exibir Extrato':
                        # Atualizando dentro do campo extrato
                        window['extrato'].update(f'Nome: {cl.nome, cl.sobrenome}'
                                                 f'\nConta: {ct.agencia}'
                                                 f'\nSaldo: R${ct.saldo:.2f}')

                    # Fazendo depósito
                    if event == 'Depositar':
                        # Fechando tela Principal
                        window.close()
                        # Abrindo tela de depósito
                        tela_depositar()
                        while True:
                            window, event, values = sg.read_all_windows()
                            # Armazenando os dados do campo na variável
                            valor_deposito = values['valor_deposito']
                            if event == sg.WIN_CLOSED:
                                exit()
                            # Saindo da tela depósito
                            if event == 'Sair':
                                window.close()
                                # Abrindo tela Principal
                                tela_principal(cl, ct)
                                break

                            # Cancelado o depósito
                            if event == 'Cancelar':
                                # Atualiza o campo deixando em branco
                                window['valor_deposito'].update('')

                            # Confirmando depósito
                            if event == 'Confirmar':
                                # Validando (O campo não pode estar vazio)
                                if valor_deposito == '':
                                    sg.Popup('Preencha todos os campos!', title='Erro')

                                else:
                                    # verificando se o campo contém apenas números
                                    if valor_deposito.isdigit():
                                        # Caso não esteja vazio, a função depositar da classe conta é chamada
                                        ct.Depositar(float(valor_deposito))
                                        sg.Popup('DEPÓSITO CONCLUÍDO!')
                                        window['valor_deposito'].update('')
                                    else:
                                        sg.Popup('DIGITE APENAS NÚMEROS')

                    # Fazendo Saque
                    if event == '   Sacar   ':
                        # Fechando tela Principal
                        window.close()
                        # Abrindo tela saque
                        tela_sacar()
                        while True:
                            window, event, values = sg.read_all_windows()
                            # Armazenando os dados do campo na variável
                            valor_saque = values['valor_saque']
                            if event == sg.WIN_CLOSED:
                                exit()
                            # Saindo da tela saque
                            if event == 'Sair':
                                window.close()
                                # Abrindo tela principal
                                tela_principal(cl, ct)
                                break

                            # Cancelado o saque
                            if event == 'Cancelar':
                                # Atualiza o campo deixando em branco
                                window['valor_saque'].update('')

                            # Confirmando Saque
                            if event == 'Confirmar':
                                # Validando (O campo não pode estar vazio)
                                if valor_saque == '':
                                    sg.Popup('Preencha todos os campos!', title='Erro')
                                else:
                                    # verificando se o campo contém apenas números
                                    if valor_saque.isdigit():
                                        # Caso não esteja vazio, a função sacar da classe conta é chamada
                                        ct.sacar(float(valor_saque))
                                        sg.Popup('SAQUE CONCLUÍDO!'
                                                 '\nRetire o Dinheiro')
                                        window['valor_saque'].update('')
                                    else:
                                        sg.Popup('DIGITE APENAS NÚMEROS')


    # Criando Conta
    if event == 'Criar conta':
        # Fechando tela de login
        window.close()
        # Abrindo tela para criar conta
        tela_criar_conta()
        while True:
            window, event, values = sg.read_all_windows()
            if event == sg.WIN_CLOSED:
                exit()
            # Fechando tela para criar conta
            if event == 'Cancelar':
                window.close()
                # Abrindo tela login
                tela_login()
                break
            # Armazenando os dados dos campos nas variávels
            nome = values['nome']
            sobrenome = values['sobrenome']
            cpf = values['cpf']
            senha = values['senha']
            repeticao_senha = values['repeticao_senha']
            # Validando senha (Não pode ficar em branco)
            if senha != '' and repeticao_senha != '':
                # Validando senha (Mínimo 6 caracteres)
                if int(len(senha)) == 6:
                    # Validando senha (Os dois campos precisam ter a mesma senha)
                    if senha == repeticao_senha and event == 'Criar Conta':
                        # Chamando função criar conta e passando os parâmetros
                        criar_conta.criar_conta(nome, sobrenome, cpf, senha, repeticao_senha)
                        # Deixando os campos em branco novamente
                        window['nome'].update('')
                        window['sobrenome'].update('')
                        window['cpf'].update('')
                        window['senha'].update('')
                        window['repeticao_senha'].update('')
                    else:
                        sg.Popup('As senhas precisam ser iguais!', font='arial 13', title='Erro')
                else:
                    sg.Popup('As senha precisar conter 6 dígitos(Números)!', font='arial 13', title='Erro')
            # Validando criação da conta. Todos os campos precisam ser preenchidos.
            elif nome == '' or sobrenome == '' or cpf == '' or senha == '' or repeticao_senha == '':
                sg.Popup('Verifique se todos os campos estão preenchidos.', font='arial 13', title='Erro')










