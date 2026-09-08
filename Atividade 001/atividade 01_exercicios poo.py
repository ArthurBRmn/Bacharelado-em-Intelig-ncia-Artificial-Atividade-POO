 # 1. Classe veiculo

class Veiculo:

    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.ano = 0
        self.velocidade_atual = 0
        self.ligado = False

    def acelerar(self, quantidade):
        if self.ligado == True:
            self.velocidade_atual += quantidade


    def frear(self,quantidade_f):
        if self.velocidade_atual > 0:
            self.velocidade_atual -= quantidade_f
        elif self.velocidade_atual <= 0:
            self.velocidade_atual = 0

# Se ligado == False vai virar True
    def ligar (self):
        if self.ligado == False:
            self.ligado = True

# Se ligado == True vai virar False e zerar a velocidade
    def desligar (self):
        if self.ligado == True:
            self.ligado = False
            self.velocidade_atual = 0

# Objeto recebe a classe
veiculo1 = Veiculo()
veiculo1.ligar()
veiculo1.acelerar(50)
veiculo1. frear(25)
print(veiculo1.velocidade_atual, veiculo1.ligado)

# 2. Classe ContaBancaria:

class ContaBancaria:
    def __init__(self):
        self.titular =''
        self.numero_conta = 0
        self.saldo = 0.0

    def depositar(self, valor):
        valor += self.saldo

    def sacar (self, valor):
        if valor <= self.saldo:
            valor -= self.saldo