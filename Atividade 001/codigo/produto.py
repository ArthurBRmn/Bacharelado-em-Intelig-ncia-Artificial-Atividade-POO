class Produto:

    def __init__(self):
        self.__nome = ''
        self.__preco = 5.50
        self.__quantidade_estoque = 0
        self.__categoria = ''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_quantidade_estoque(self):
        return self.__quantidade_estoque

    def set_quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque (self,quantidade):
        self.__quantidade_estoque += quantidade

    def remover_estoque (self, quantidade_r):

        if quantidade_r <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade_r

    def aplicar_desconto (self, valor_d):
        self.__preco *= 1 - valor_d / 100