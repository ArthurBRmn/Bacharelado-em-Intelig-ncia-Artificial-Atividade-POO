from codigo.heranca import *


def test_deve_retornar_matricula_aluno():
    aluno = Aluno()
    aluno.set_matricula(123)

    assert aluno.get_matricula() == 123


def test_deve_retornar_titulacao_professor():
    professor = Professor()
    professor.set_titulacao("Doutorado")

    assert professor.get_titulacao() == "Doutorado"


def test_deve_retornar_nome_pessoa():
    pessoa = Pessoa()
    pessoa.set_nome("Marco")

    assert pessoa.get_nome() == "Marco"


def test_deve_retornar_nome_aluno():
    aluno = Aluno()
    aluno.set_nome("Sara")

    assert aluno.get_nome() == "Sara"


def test_deve_retornar_nome_professor():
    professor = Professor()
    professor.set_nome("Ana")

    assert professor.get_nome() == "Ana"

def test_aluno_ensino_medio_aprovado():
    aluno = AlunoEnsinoMedio()

    aluno.set_nota1(7)
    aluno.set_nota2(8)

    assert aluno.calcular_media() == 7.5
    assert aluno.foi_aprovado() is True


def test_aluno_ensino_medio_reprovado():
    aluno = AlunoEnsinoMedio()

    aluno.set_nota1(5)
    aluno.set_nota2(6)

    assert aluno.calcular_media() == 5.5
    assert aluno.foi_aprovado() is False


def test_aluno_graduacao_aprovado():
    aluno = AlunoGraduacao()

    aluno.set_nota1(8)
    aluno.set_nota2(7)

    assert aluno.calcular_media() == 7.5
    assert aluno.foi_aprovado() is True


def test_aluno_graduacao_reprovado():
    aluno = AlunoGraduacao()

    aluno.set_nota1(6)
    aluno.set_nota2(7)

    assert aluno.calcular_media() == 6.5
    assert aluno.foi_aprovado() is False


def test_aluno_ensino_medio_com_media_6_aprovado():
    aluno = AlunoEnsinoMedio()

    aluno.set_nota1(6)
    aluno.set_nota2(6)

    assert aluno.foi_aprovado() is True


def test_aluno_graduacao_com_media_7_aprovado():
    aluno = AlunoGraduacao()

    aluno.set_nota1(7)
    aluno.set_nota2(7)

    assert aluno.foi_aprovado() is True