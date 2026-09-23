class Pessoa:

    def __init__(self):

        self.__nome = ''
        self.__idade = 0
        self.__altura = 0.0
        self.__peso = 0.0

        def get_nome(self):
            return self.__nome

        def set_nome(self, nome):
            self.__nome = nome

        def get_idade(self):
            return self.__idade

        def set_idade(self, idade):
            self.__idade = idade

        def get_altura(self):
            return self.__altura

        def set_altura(self, altura):
            self.__altura = altura

        def get_peso(self):
            return self.__peso

        def set_peso(self, peso):
            self.__peso = peso

    def envelhecer (self):
        self.__idade += 1

    def crescer (self, centimetro):
        if self.__idade < 21:
            self.__altura += centimetro

    def ganhar_peso (self , quilos):
        self.__peso += quilos

    def perder_peso (self, quilos_p):
        self.__peso -= quilos_p
