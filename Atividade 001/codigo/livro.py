class Livro:

    def __init__(self):

        self.__titulo = ''
        self.__autor =''
        self.__ano_publicacao = 0
        self.__numero_paginas = 170
        self.__genero = ''

        self.__pagina_atual = 5

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_numero_paginas(self):
        return self.__numero_paginas
    def set_numero_paginas(self, numero_paginas):
        self.__numero_paginas = numero_paginas

    def get_ano_publicacao(self):
        return self.__ano_publicacao
    def set_ano_publicacao(self, ano_publicacao):
        self.__ano_publicacao = ano_publicacao


    def abrir (self):
        print('test')

    def fechar (self):
        print('test')

    def marcar_pagina (self,pagina):
        if self.__numero_paginas >= pagina:
            self.__pagina_atual = pagina

    def avancar_pagina (self):
        if self.__pagina_atual < self.__numero_paginas:
            self.__pagina_atual += 1

    def retroceder_pagina (self):
        if self.__pagina_atual > 1:
            self.__pagina_atual -= 1