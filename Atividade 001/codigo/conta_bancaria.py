class ContaBancaria:
    def __init__(self):
        self.titular =''
        self.numero_conta = 0
        self.saldo = 0

    def depositar (self, valor):
        self.saldo += valor
        print(f'Depositado com sucesso: {valor} R$, o seu saldo: {self.saldo}\n')

    def sacar (self, valor_r):
        if valor_r <= self.saldo:
            self.saldo -= valor_r
            print(f'saque: {valor_r} R$, o seu saldo: {self.saldo}\n')