# Importando módulo para gerar números aleatórios (número da conta).
import random
# Importando módulo para criar as interfaces.
import PySimpleGUI as sg


# Função para criar a conta do cliente
def criar_conta(nome, sobrenome, cpf, senha, repeticao_senha):
    while True:
        # Condição para as senhas serem iguais.
        if repeticao_senha == senha:
            break
        else:
            print('As senhas precisam ser iguais')
            repeticao_senha = str(input('Digite a senha novamente: '))
    # Gerando o número da conta
    num = random.randint(1000, 9999)
    dig = random.randint(1, 9)
    # Juntando o número
    agencia = f'{num}-{dig}'
    saldo = 0
    # Armazenando os dados do clientes através de arquivos txt
    with open(f'{agencia}.txt', 'w') as arq:
        arq.write(f'{agencia} \n{senha} \n{nome.capitalize()} \n{sobrenome} \n{cpf}')
    with open(f'{agencia}.txt', 'r') as arq:
        mensagem = arq.readlines()
        # Menagem exibibida caso o usuário conclua a criação da conta
        sg.Popup('ABERTURA DE CONTA COM SUCESSO!'
                 f'\nConta: {mensagem[0]}'
                 f'\nNome: {mensagem[2]}{mensagem[3]}'
                 f'\nFaça LOGIN e comece a usar a conta.', font='arial 13', title='Conta Criada')


# Função para fazer login
def login(agencia, senha):
    # Tentativa de abrir o arquivo txt com o numero da agencia
    try:
        # Abrindo arquivo
        with open(f'{agencia}.txt', 'r') as arq:
            # Puxando os dados
            mensagem = arq.readlines()
            # Verificando se a senha digitada no login é igual a senha da criação da conta
            if int(mensagem[1]) == int(senha):
                # Abrindo arquivo novamente
                with open(f'{agencia}.txt', 'r') as arquivo:
                    mensagem = arquivo.readlines()
                # Retornando os dados
                return mensagem
    except:
        # Caso nao seja possivel abrir, essa mensagem será exibida na tela
        sg.Popup('ERRO AO TENTAR ACESSAR A CONTA!'
                 '\nAgência inválida.', font='arial 13')

    else:
        # Exibindo mensagem caso as senhas sejam diferentes
        sg.Popup('SENHA INVÁLIDA!', title='Erro')
        return False






