class Conta:
    # Função construtora
    # Self é a referência para encontrar o objeto em memória
    def __init__(self, numero, titular, saldo, limite):
        print(self)
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
