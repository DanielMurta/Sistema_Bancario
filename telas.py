import PySimpleGUI as sg
import Cliente


def tela_login():
    sg.theme('DarkRed1')

    frame_layout = [
        [sg.T('Agência', font='arial 16')],
        [sg.InputText(key='agencia', font='arial 16', size=18), sg.T('-'), sg.InputText(key='agencia2', font='arial 16',
                                                                                        size=3)],
        [sg.T('Senha', font='arial 16')],
        [sg.InputText(key='senha', font='arial 16', size=18)],
        [sg.Button('Login', font='arial 16')]
    ]

    layout = [
        [sg.Text("Banco Brazesco", font='arial 20')],
        [sg.Frame('Login', frame_layout)],
        [sg.Text('Não possuiu conta?', font='arial 16')],
        [sg.Button('Criar conta', font='arial 16')]
    ]

    return sg.Window('Caixa Brazesco', layout, size=(500, 400), element_justification='center', finalize=True)


def tela_principal(cliente, conta):
    sg.theme('DarkRed1')

    coluna1 = [
        [sg.Button("Depositar", font='arial 16')]
    ]

    coluna2 = [
        [sg.Text(f'Olá, {cliente.nome}{cliente.sobrenome}', font='arial 14')],
        [sg.Text(f'Conta: {conta.agencia}', font='arial 14')],
        [sg.Text('O que deseja fazer?', font='arial 14')]
    ]

    coluna3 = [
        [sg.Button('   Sacar   ', font='arial 16')]
    ]

    layout_menu = [
        [sg.Column(layout=coluna1), sg.Column(layout=coluna2, pad=(10, 10)), sg.Column(layout=coluna3)],
        [sg.Button('Exibir Extrato', font='arial 13')],
        [sg.Output(key='extrato', size=(40, 4), font='arial 16')],
        [sg.Button('Sair', font='arial 16')]
    ]
    return sg.Window('Menu caixa', layout_menu, size=(500, 400), element_justification='Center', finalize=True)


def tela_criar_conta():
    sg.theme('DarkRed1')

    frame_layout = [
        [sg.Text('Nome', font='arial 16')],
        [sg.InputText(key='nome', font='arial 16', size=35)],
        [sg.Text('Sobrenome', font='arial 16')],
        [sg.InputText(key='sobrenome', font='arial 16', size=35)],
        [sg.Text('cpf', font='arial 16')],
        [sg.InputText(key='cpf', font='arial 16', size=35)],
        [sg.Text('Senha', font='arial 16')],
        [sg.InputText(key='senha', font='arial 16', size=35)],
        [sg.Text('Digite a senha novamente', font='arial 16')],
        [sg.InputText(key='repeticao_senha', font='arial 16', size=35)],
    ]

    layout_criarconta = [
        [sg.Text("Crie sua conta", font='arial 18')],
        [sg.Frame('Login', frame_layout)],
        [sg.Button('Criar Conta', font='arial 16'), sg.Button('Cancelar', font='arial 16')],
        [sg.Text('', key='msg_criar_conta')]

    ]
    window_criarconta = sg.Window('Criar conta', layout_criarconta, size=(500, 500), element_justification='center',
                                  finalize=True)


def tela_depositar():
    sg.theme('DarkRed1')

    frame_layout = [
        [sg.Text('Valor:', font='arial 16')],
        [sg.InputText('', key='valor_deposito', font='arial 16', size=18)],
        [sg.Button('Confirmar', font='arial 16'), sg.Button('Cancelar', font='arial 16')]
    ]

    layout_deposito = [
        [sg.Text('Depósito Brazesco', font='arial 18')],
        [sg.Frame('-', frame_layout)],
        [sg.Button('Sair', font='arial 16')]
    ]

    window_deposito = sg.Window('Depósito', layout_deposito, size=(400, 300), element_justification='Center',
                                finalize=True)


def tela_sacar():
    sg.theme('DarkRed1')

    frame_layout = [
        [sg.Text('Valor:', font='arial 16')],
        [sg.InputText('', key='valor_saque', font='arial 16', size=18)],
        [sg.Button('Confirmar', font='arial 16'), sg.Button('Cancelar', font='arial 16')]
    ]

    layout_deposito = [
        [sg.Text('Saque Brazesco', font='arial 18')],
        [sg.Frame('-', frame_layout)],
        [sg.Button('Sair', font='arial 16')]
    ]

    window_saque = sg.Window('Saque', layout_deposito, size=(400, 300), element_justification='Center',
                             finalize=True)
