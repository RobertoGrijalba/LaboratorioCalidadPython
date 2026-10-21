def validar_nombre(nombre):
    if not isinstance(nombre, str):
        raise ValueError("El nombre debe ser texto")

    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío")

    return True


def validar_edad(edad):
    if not isinstance(edad, int) or isinstance(edad, bool):
        raise ValueError("La edad debe ser un número entero")

    if edad < 18:
        raise ValueError("La edad debe ser mayor o igual a 18")

    if edad > 120:
        raise ValueError("La edad ingresada no es válida")

    return True


def validar_precio(precio):
    if not isinstance(precio, (int, float)) or isinstance(precio, bool):
        raise ValueError("El precio debe ser numérico")

    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    return True


def validar_porcentaje(porcentaje):
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")

    return True