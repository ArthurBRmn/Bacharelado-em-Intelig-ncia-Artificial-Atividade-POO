from codigo.conta_bancaria import *

def test_modificar_titular():
    conta_bancaria = ContaBancaria()
    conta_bancaria.set_titular("Carlos")
    assert conta_bancaria.get_titular() == "Carlos"

def test_modificar_numero_conta():
    conta_bancaria = ContaBancaria()
    conta_bancaria.set_numero_conta(5)
    assert conta_bancaria.get_numero_conta() == 5

def test_modificar_saldo_conta():
    conta_bancaria = ContaBancaria()
    conta_bancaria.set_saldo(100)
    assert conta_bancaria.get_saldo() == 100

def test_deposito_conta():
    conta_bancaria = ContaBancaria()
    conta_bancaria.depositar(200)
    assert conta_bancaria.get_saldo() == 200

def test_varios_depositos_conta():
    conta_bancaria = ContaBancaria()
    conta_bancaria.depositar(200)
    conta_bancaria.depositar(100)
    assert conta_bancaria.get_saldo() == 300

def test_saque_conta_sem_saldo():
    conta_bancaria = ContaBancaria()
    conta_bancaria.sacar(100)
    assert conta_bancaria.get_saldo() == 0

def test_saque_conta_com_saldo_():
    conta_bancaria = ContaBancaria()
    conta_bancaria.depositar(200)
    conta_bancaria.sacar(100)
    assert conta_bancaria.get_saldo() == 100