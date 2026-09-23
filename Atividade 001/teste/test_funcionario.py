from codigo.funcionario import *

def test_modificar_nome():
    funcionario01 = Funcionario()
    funcionario01.set_nome("Carlos")
    assert funcionario01.get_nome() == "Carlos"

def test_modificar_cargo():
    funcionario01 = Funcionario()
    funcionario01.set_cargo("Desenvolvedor")
    assert funcionario01.get_cargo() == "Desenvolvedor"

def test_modificar_salario():
    funcionario01 = Funcionario()
    funcionario01.set_salario(5000.0)
    assert funcionario01.get_salario() == 5000.0

def test_modificar_departamento():
    funcionario01 = Funcionario()
    funcionario01.set_departamento("TI")
    assert funcionario01.get_departamento() == "TI"

def test_receber_aumento():
    funcionario01 = Funcionario()
    funcionario01.set_salario(4000.0)
    funcionario01.receber_aumento(10)  # 10% de aumento sobre 4000
    assert funcionario01.get_salario() == 4400.0

def test_mudar_departamento():
    funcionario01 = Funcionario()
    funcionario01.set_departamento("RH")
    funcionario01.mudar_departamento("Financeiro")
    assert funcionario01.get_departamento() == "Financeiro"

def test_exibir_dados():
    funcionario01 = Funcionario()
    funcionario01.set_nome("Ana")
    funcionario01.set_cargo("Gerente")
    funcionario01.set_salario(8000.0)
    funcionario01.set_departamento("Vendas")
    resultado = funcionario01.exibir_dados()
    assert resultado == "Nome: Ana, Cargo: Gerente, Salário: 8000.0, Departamento: Vendas"