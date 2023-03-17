# Función
def funcion(param1, param2):
    return param1 + param2


# Funciones de primera clase
def funcion_primera_clase():
    return


variable = funcion_primera_clase
variable()


# Funciones anidadas
def funcion_principal():

    nombre = "Ana"

    def funcion_anidada():
        print(nombre)

    funcion_anidada()


# Funciones de orden superior
def saludar():

    mensaje = "Buen día"

    def imprimir_saludo():
        print(mensaje)

    return imprimir_saludo
