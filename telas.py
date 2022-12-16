import PySimpleGUI as sg
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


def tela_principal():
    layout_menu = [
        [sg.Text("Banco Brazesco", font='arial 15')],
    ]
    return sg.Window('Menu caixa', layout_menu, finalize=True)


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
        [sg.Text("Crie sua conta", font='arial 15')],
        [sg.Frame('Login', frame_layout)],
        [sg.Button('Criar Conta'), sg.Button('Cancelar')],
        [sg.Text('', key='msg_criar_conta')]

    ]
    window_criarconta = sg.Window('Criar conta', layout_criarconta, size=(400, 400), element_justification='center',
                                  finalize=True)
