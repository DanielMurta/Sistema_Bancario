from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca
from Banco import Banco

Banco = Banco()

Nome = str(input('Nome: '))
Idade = int(input('Idade: '))
Cliente1 = Cliente(Nome, Idade)

print('INFORMAÇÕES DA CONTA:')
Ag = int(input('Agência: '))
Ct = int(input('Conta: '))
Conta1 = ContaPoupanca(Ag, Ct, 0)


Cliente1.inserir_conta(Conta1)
Banco.InserirClientes(Cliente1)
Banco.InserirConta(Conta1)

while True:
    print('[1] Depositar [2] Sacar [3] Saldo')
    r = int(input('Opção: '))
    if r == 0:
        break
    if r == 1:
        if Banco.autenticar(Cliente1):
            Deposito = float(input('Valor do Depósito: '))
            Cliente1.conta.Depositar(Deposito)
        else:
            print('Cliente não autenticado')
    if r == 2:
        if Banco.autenticar(Cliente1):
            Saque = float(input('Valor do Saque: '))
            Cliente1.conta.sacar(Saque)
        else:
            print('Cliente não autenticado')
    if r == 3:
        if Banco.autenticar(Cliente1):
            Cliente1.conta.Informacoes()
        else:
            print('Cliente não autenticado')



