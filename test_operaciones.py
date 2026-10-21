import pytest

from operaciones import sumar, restar, multiplicar, dividir, calcular_descuento


def test_sumar():
    assert sumar(5, 3) == 8


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(4, 3) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_division_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_calcular_descuento():
    assert calcular_descuento(100, 20) == 80


def test_precio_negativo():
    with pytest.raises(ValueError):
        calcular_descuento(-100, 20)


def test_porcentaje_invalido():
    with pytest.raises(ValueError):
        calcular_descuento(100, 150)