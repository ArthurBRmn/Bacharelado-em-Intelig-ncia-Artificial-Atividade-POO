class Veiculo:

    def __init__(self):
        self.__marca = ''
        self.__modelo = ''
        self.__ano = 0
        self.__velocidade_atual = 0
        self.__ligado = False

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_velocidade_atual(self):
        return self.__velocidade_atual

    def set_velocidade_atual(self, velocidade_atual):
        self.__velocidade_atual = velocidade_atual

    def get_ligado(self):
        return self.__ligado

    def set_ligado(self, ligado):
        self.__ligado = ligado

    def acelerar (self, quantidade):
        if self.__ligado == True:
            self.__velocidade_atual += quantidade

    def frear (self,quantidade_f):
        self.__velocidade_atual -= quantidade_f

        if self.__velocidade_atual < 0:
            self.__velocidade_atual = 0

# Se ligado == False vai virar True
    def ligar (self):
        if self.__ligado == False:
            self.__ligado = True


# Se ligado == True vai virar False e zerar a velocidade
    def desligar (self):
        if self.__ligado == True:
            self.__ligado = False
            self.__velocidade_atual = 0
