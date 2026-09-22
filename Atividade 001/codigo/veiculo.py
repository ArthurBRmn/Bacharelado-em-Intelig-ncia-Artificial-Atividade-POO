class Veiculo:

    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.ano = 0
        self.velocidade_atual = 0
        self.ligado = False

    def acelerar (self, quantidade):
        if self.ligado == True:
            self.velocidade_atual += quantidade
            print(f'Velocidade atual: {self.velocidade_atual}\n')

    def frear (self,quantidade_f):
        self.velocidade_atual -= quantidade_f

        if self.velocidade_atual < 0:
            self.velocidade_atual = 0

        print(f'Velocidade atual: {self.velocidade_atual}\n')

# Se ligado == False vai virar True
    def ligar (self):
        if self.ligado == False:
            self.ligado = True
            print('Carro ligou\n')

# Se ligado == True vai virar False e zerar a velocidade
    def desligar (self):
        if self.ligado == True:
            self.ligado = False
            self.velocidade_atual = 0
            print('Carro desligou\n')