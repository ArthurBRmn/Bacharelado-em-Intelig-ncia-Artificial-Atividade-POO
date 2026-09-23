from codigo.pessoa import *

def test_modificar_nome():
    pessoa1 = Pessoa()
    pessoa1.set_nome("Samuel")
    assert pessoa1.get_nome() == "Samuel"

def test_modificar_idade():
    pessoa1 = Pessoa()
    pessoa1.set_idade(21)
    assert pessoa1.get_idade() == 21

def test_modificar_altura():
    pessoa1 = Pessoa()
    pessoa1.set_altura(1.67) # omg
    assert pessoa1.get_altura() == 1.67

def test_modificar_peso():
    pessoa1 = Pessoa()
    pessoa1.set_peso(120.7) #os 0.7 kgs salvando os 40 kg de gordura
    assert pessoa1.get_peso() == 120.7

def test_envelhecer_idade_pessoa():
    pessoa1 = Pessoa()
    pessoa1.set_idade(19)
    pessoa1.envelhecer()
    assert pessoa1.get_idade() == 20

def test_crescer_altura_pessoa():
    pessoa1 = Pessoa()
    pessoa1.set_idade(12)
    pessoa1.crescer(0.90)
    assert pessoa1.get_altura() == 0.9 # um anao

def test_crescer_altura_fora_da_idade_pessoa():
    pessoa1 = Pessoa()
    pessoa1.set_idade(24) # sai daqui velho vai aumentar nao
    pessoa1.crescer(200)
    assert pessoa1.get_altura() == 0
    # nao tem como aumentar a idade depois dos 21 anos

def test_ganhar_peso():
    pessoa1 = Pessoa()
    pessoa1.set_peso(70)
    pessoa1.ganhar_peso(20)
    assert pessoa1.get_peso() == 90

def test_perder_peso():
    pessoa1 = Pessoa()
    pessoa1.set_peso(70)
    pessoa1.perder_peso(20)
    assert pessoa1.get_peso() == 50