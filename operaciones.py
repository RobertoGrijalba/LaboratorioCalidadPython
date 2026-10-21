def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def calcular_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("Porcentaje inválido")
    descuento = precio * porcentaje / 100
    return precio - descuento