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
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo {} titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __verifica_saldo_valido(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def sacar(self, valor):
        if self.__verifica_saldo_valido(valor):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def transferir(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return {"BB": "001"}
