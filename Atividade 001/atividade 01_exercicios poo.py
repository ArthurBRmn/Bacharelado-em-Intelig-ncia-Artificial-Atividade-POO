 # 1. Classe veiculo

class Veiculo:

    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.ano = 0
        self.velocidade_atual = 0
        self.ligado = False

    def acelerar(self, quantidade):
        self.velocidade_atual += quantidade

    def frear(self, quantidade_f):
        if self.velocidade_atual <= 0:
            self.velocidade_atual = 0

    def ligar (self):
        self.ligado = True