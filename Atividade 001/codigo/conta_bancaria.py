class ContaBancaria:
    def __init__(self):
        self.__titular =''
        self.__numero_conta = 0
        self.__saldo = 0

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_numero_conta(self):
        return self.__numero_conta

    def set_numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor

    def depositar (self, valor):
        self.__saldo += valor

    def sacar (self, valor_r):
        if valor_r <= self.__saldo:
            self.__saldo -= valor_r