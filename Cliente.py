import Conta

class Cliente():
    def __init__(self, nome, sobrenome, cpf, senha, repetucao_senha):
        super().__init__(nome, sobrenome)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta








