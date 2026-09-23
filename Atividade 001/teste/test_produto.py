from codigo.produto import *

def test_modificar_nome():
    produto1 = Produto()
    produto1.set_nome("Pedro")
    assert produto1.get_nome() == "Pedro"

def test_modificar_categoria():
    produto1 = Produto()
    produto1.set_categoria("Estoque Fresco")
    assert produto1.get_categoria() == "Estoque Fresco"

def test_modificar_preco():
    produto1 = Produto()
    produto1.set_preco(50)
    assert produto1.get_preco() == 50

def test_quantidade_estoque():
    produto1 = Produto()
    produto1.set_quantidade_estoque(400)
    assert produto1.get_quantidade_estoque() == 400

def test_adicionar_estoque():
    produto1 = Produto()
    produto1.set_quantidade_estoque(20)
    produto1.adicionar_estoque(20)
    assert produto1.get_quantidade_estoque() == 40

def test_remover_estoque():
    produto1 = Produto()
    produto1.set_quantidade_estoque(20)
    produto1.remover_estoque(5)
    assert produto1.get_quantidade_estoque() == 15

def test_remover_estoque_sem_estoque():
    produto1 = Produto()
    produto1.set_quantidade_estoque(5)
    produto1.remover_estoque(10)
    assert produto1.get_quantidade_estoque() == 5
    # nem se mexe no estoque porque não da pra retirar mais doq ja se tem :/

def test_aplicar_desconto():
    produto1 = Produto()
    produto1.set_preco(400)
    produto1.aplicar_desconto(50)
    assert produto1.get_preco() == 200