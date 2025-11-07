class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
        if self.saldo < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
    
    def depositar(self, valor):
        """Deposita um valor na conta."""
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self.saldo += valor

 

  