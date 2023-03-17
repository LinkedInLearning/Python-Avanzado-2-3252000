# Scope global
fecha = "01-01-2000"


def funcion_scope_local():
    # Scope local
    nombre = "Ana"
    return nombre


def funcion_principal():

    nombre = "Ana"

    def funcion_anidada():
        print(nombre)

    funcion_anidada()


funcion_principal()


def saludar():

    mensaje = "Buen día"

    def imprimir_saludo():
        print(mensaje)

    return imprimir_saludo


saludo = saludar()
saludo()
