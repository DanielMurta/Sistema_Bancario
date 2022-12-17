import PySimpleGUI as sg
import Cliente
def tela_login():
    sg.theme('DarkRed1')

    frame_layout = [
        [sg.T('Agência')],
        [sg.InputText(key='agencia', size=15), sg.T('-'), sg.InputText(key='agencia2', size=3)],
        [sg.T('Senha')],
        [sg.InputText(key='senha', size=15)],
        [sg.Button('Login')]
    ]

    layout = [
        [sg.Text("Banco Brazesco", font='arial 15')],
        [sg.Frame('Login', frame_layout)],
        [sg.Text('Não possuiu conta?', font='arial 10')],
        [sg.Button('Criar conta')]
    ]

    return sg.Window('Caixa Brazesco', layout, size=(400, 300), element_justification='center', finalize=True)


def tela_principal(cliente, conta):
    sg.theme('DarkRed1')

    coluna1 = [
        [sg.Button("Depositar", font='arial 13')]
    ]

    coluna2 = [
        [sg.Text(f'Olá, {cliente.nome}{cliente.sobrenome}', font='arial 11')],
        [sg.Text(f'Conta: {conta.agencia}', font='arial 11')],
        [sg.Text('O que deseja fazer?', font='arial 11')]
    ]

    coluna3 = [
        [sg.Button('   Sacar   ', font='arial 13')]
    ]

    layout_menu = [
        [sg.Column(layout=coluna1), sg.Column(layout=coluna2, pad=(10, 10)), sg.Column(layout=coluna3)],
        [sg.Button('Exibir Extrato', font='arial 13')],
        [sg.Output(key='extrato', size=(40, 4), font='arial 13')],
        [sg.Button('Sair', font='arial 13')]
    ]
    return sg.Window('Menu caixa', layout_menu, size=(400, 300), element_justification='Center', finalize=True)


def tela_criar_conta():
    sg.theme('DarkRed1')

    frame_layout = [
        [sg.Text('Nome')],
        [sg.InputText(key='nome', size=20)],
        [sg.Text('Sobrenome')],
        [sg.InputText(key='sobrenome', size=20)],
        [sg.Text('cpf')],
        [sg.InputText(key='cpf', size=20)],
        [sg.Text('Senha')],
        [sg.InputText(key='senha', size=20)],
        [sg.Text('Digite a senha novamente')],
        [sg.InputText(key='repeticao_senha', size=20)],
    ]

    layout_criarconta = [
        [sg.Text("Crie sua conta", font='arial 13')],
        [sg.Frame('Login', frame_layout)],
        [sg.Button('Criar Conta'), sg.Button('Cancelar')],
        [sg.Text('', key='msg_criar_conta')]

    ]
    window_criarconta = sg.Window('Criar conta', layout_criarconta, size=(400, 400), element_justification='center',
                                  finalize=True)
