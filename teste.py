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


