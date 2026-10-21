usuarios = []


def registrar_usuario(nombre, edad):
    if nombre == "":
        raise ValueError("El nombre es obligatorio")

    if edad < 18:
        raise ValueError("El usuario debe ser mayor de edad")

    usuario = {
        "nombre": nombre,
        "edad": edad
    }

    usuarios.append(usuario)
    return usuario


def listar_usuarios():
    return usuarios


def buscar_usuario(nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario
    return None


def contar_usuarios():
    return len(usuarios)