from codigo.veiculo import *

def test_deve_modificar_marca_veiculo():
    veiculo = Veiculo()
    veiculo.set_marca("Volkswagen")
    assert veiculo.get_marca() == "Volkswagen"

def test_deve_modificar_modelo_veiculo():
    veiculo = Veiculo()
    veiculo.set_modelo("Tiguan")
    assert veiculo.get_modelo() == "Tiguan"

def test_deve_modificar_ano_veiculo():
    veiculo = Veiculo()
    veiculo.set_ano(2025)
    assert veiculo.get_ano() == 2025

def test_deve_modificar_velocidade_atual_veiculo():
    veiculo = Veiculo()
    veiculo.set_velocidade_atual(50)
    assert veiculo.get_velocidade_atual() == 50

def test_deve_modificar_ligacao_veiculo():
    veiculo = Veiculo()
    veiculo.set_ligado(True)
    assert veiculo.get_ligado() == True

def test_deve_acelerar_veiculo():
    veiculo = Veiculo()
    veiculo.acelerar(100)
    assert veiculo.get_velocidade_atual() == 100

def test_deve_acelerar_veiculo_novamente():
    veiculo = Veiculo()
    veiculo.acelerar(100)
    veiculo.acelerar(20)
    assert veiculo.get_velocidade_atual() == 120

def test_deve_frear_veiculo():
    veiculo = Veiculo()
    veiculo.acelerar(100)
    veiculo.frear(20)
    assert veiculo.get_velocidade_atual() == 80

def test_deve_frear_veiculo_novamente():
    veiculo = Veiculo()
    veiculo.acelerar(100)

    veiculo.frear(20)
    veiculo.frear(10)
    assert veiculo.get_velocidade_atual() == 70

def test_deve_frear_veiculo_acima_velocidade_atual():
    veiculo = Veiculo()
    veiculo.acelerar(100)
    veiculo.frear(120)
    assert veiculo.get_velocidade_atual() == 0