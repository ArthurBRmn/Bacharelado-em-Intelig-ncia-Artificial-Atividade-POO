class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__cpf = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf


class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__matricula = 0
        self.__escola_segundo_grau = ""
        self.__nota1 = 0
        self.__nota2 = 0

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_escola_segundo_grau(self):
        return self.__escola_segundo_grau

    def set_escola_segundo_grau(self, escola_segundo_grau):
        self.__escola_segundo_grau = escola_segundo_grau

    def get_nota1(self):
        return self.__nota1

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def get_nota2(self):
        return self.__nota2

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    # Calcula a média das duas notas
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2


class AlunoEnsinoMedio(Aluno):
    def __init__(self):
        Aluno.__init__(self)

    # No ensino médio, aprovação ocorre com média >= 6
    def foi_aprovado(self):
        return self.calcular_media() >= 6


class AlunoGraduacao(Aluno):
    def __init__(self):
        Aluno.__init__(self)

    # Na graduação, aprovação ocorre com média >= 7
    def foi_aprovado(self):
        return self.calcular_media() >= 7


class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__titulacao = ""

    def get_titulacao(self):
        return self.__titulacao

    def set_titulacao(self, titulacao):
        self.__titulacao = titulacao