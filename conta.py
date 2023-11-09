class Conta:
    # Função construtora
    # Self é a referência para encontrar o objeto em memória
    def __init__(self, numero, titular, saldo, limite):
        print(self)
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
