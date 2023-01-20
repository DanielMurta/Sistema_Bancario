# Importação do método abstrato
from abc import ABC, abstractmethod

# Criação da classe conta
class Conta(ABC):
    # Definindo função inicializadora(Atributos)
    def __init__(self, agencia, senha, cliente, saldo):
        self.agencia = agencia
        self.senha = senha
        self.saldo = saldo
        self.cliente = cliente

    # Função p/ Depositar
    def Depositar(self, valor):
        self.saldo += valor

    # Função com método abstrato para "forçar" outra classe a implementa-lo
    @abstractmethod
    def sacar(self, valor): pass


# Criando classe Poupança.
class ContaPoupanca(Conta):

    # Função para sacar (Atraves do método abstrato)
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor






