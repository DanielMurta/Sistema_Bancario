from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca
import criar_conta
import PySimpleGUI as sg

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

window = sg.Window('Caixa Bradisco', layout, size=(400, 300), element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Login':
        agencia = int(values['agencia'])
        senha = int(values['senha'])
        criar_conta.login(agencia, senha)
        with open(f'{agencia}.txt', 'r') as arq:
            mensagem = arq.readlines()
            cl = Cliente(mensagem[2], mensagem[3], mensagem[4], mensagem[1], mensagem[1])
        ct = ContaPoupanca(agencia, senha, cl, saldo=0)
        sg.theme('DarkRed1')
        layout_menu = [
            [sg.Text("Banco Brazesco", font='arial 15')],
        ]
        window_menu = sg.Window('Menu caixa', layout_menu)
        while True:
            event, values = window_menu.read()
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
        sg.theme('DarkRed1')
        layout_criarconta = [
            [sg.Text("Crie sua conta", font='arial 15')],
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
            [sg.Button('Criar Conta'), sg.Button('Cancelar')]
        ]
        window_criarconta = sg.Window('Criar conta', layout_criarconta, element_justification='center')
        while True:
            event, values = window_criarconta.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Cancelar':
                break
            nome = str(values['nome'])
            sobrenome = str(values['sobrenome'])
            cpf = int(values['sobrenome'])
            senha = int(values['senha'])
            repeticao_senha = int(values['repeticao_senha'])
            criar_conta.criar_conta(nome, sobrenome, cpf, senha, repeticao_senha)







