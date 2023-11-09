class Conta:
    # Função construtora
    # Self é a referência para encontrar o objeto em memória
    def __init__(self, numero, titular, saldo, limite):
        # O "__" define que o atributo é privado. O Python apenas o identifica e o
        # desenvolvedor por conciência deve saber que o atributo idenficado não
        # deve ser usado fora da classe.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if not valor <= self.__saldo:
            if not valor <= self.__limite:
                print("Saldo insuficiente")
            else:
                self.__limite -= valor
        else:
            self.__saldo -= valor

    def transferir(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_numero(self, numero):
        self.__numero = numero

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite
