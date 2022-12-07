from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca
from Banco import Banco
import criar_conta

while True:
    print('[1] LOGIN')
    print('[2] CRIAR CONTA')
    resp = int(input('Opção: '))
    if resp == 1:
        print('-----LOGIN-----')
        agencia = int(input('Agência: '))
        senha = int(input('Senha: '))
        Banco.autenticar(agencia, senha)
    if resp == 2:
        criar_conta.criar_conta()





while True:
    print('[1] Depositar [2] Sacar [3] Saldo')
    r = int(input('Opção: '))
    if r == 0:
        break
    if r == 1:
        pass




