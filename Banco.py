class Banco:
    def __init__(self):
        self.cliente = []
        self._agencia = []
        self.contas = []

    def InserirClientes(self, cliente):
        self.cliente.append(cliente)

    def InserirConta(self, conta):
        self.contas.append(conta)

    def autenticar(self, agencia, senha):

        while self.cliente not in self._agencia:  # Verifica se o cliente digitado já está cadastrado
            print('\033[33mVocê precisa digitar o nome de um cliente já cadastrado!\033[m')
            nome_cliente = str(input('Nome do ciente: ')).strip().lower()
        print('-' * 34)
        with open(f'{nome_cliente}.txt', 'r') as arq:  # Abre o arquivo do cliente digitado
            for i in arq:  # Printa as informações do cliente na tela
                print(i)

        return True
