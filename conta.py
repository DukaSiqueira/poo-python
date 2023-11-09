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
        self.__saldo -= valor
