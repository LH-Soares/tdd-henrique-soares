import pytest
from conta_bancaria import ContaBancaria

@pytest.fixture
def contas():
    conta_joao = ContaBancaria("João", 1000)
    conta_maria = ContaBancaria("Maria", 500)
    return conta_joao, conta_maria


def test_depositar(contas):
    conta_joao, _ = contas
    conta_joao.depositar(500)
    assert conta_joao.saldo == 1500

def test_sacar(contas):
    conta_joao, _ = contas
    conta_joao.sacar(300)
    assert conta_joao.saldo == 700

def test_consultar_saldo(contas):
    conta_joao, _ = contas
    assert conta_joao.consultar_saldo() == 1000

def test_transferir(contas):
    conta_joao, conta_maria = contas
    conta_joao.transferir(conta_maria, 300)
    assert conta_joao.saldo == 700
    assert conta_maria.saldo == 800

def test_depositar_valor_invalido(contas):
    conta_joao, _ = contas
    with pytest.raises(ValueError, match="maior que zero"):
        conta_joao.depositar(0)


def test_sacar_saldo_insuficiente(contas):
    conta_joao, _ = contas
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta_joao.sacar(2000)


def test_transferir_saldo_insuficiente(contas):
    conta_joao, conta_maria = contas
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta_joao.transferir(conta_maria, 2000)


def test_transferir_valor_invalido(contas):
    conta_joao, conta_maria = contas
    with pytest.raises(ValueError, match="maior que zero"):
        conta_joao.transferir(conta_maria, 0)


def test_saldo_inicial_invalido():
    with pytest.raises(ValueError, match="saldo inicial não pode ser negativo"):
        ContaBancaria("Carlos", -100)
