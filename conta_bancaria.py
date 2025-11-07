class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
        if self.saldo < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.saldo -= valor

    def consultar_saldo(self):
        return self.saldo

    def transferir(self, conta_destino, valor):
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para transferência.")
        self.sacar(valor)
        conta_destino.depositar(valor)
