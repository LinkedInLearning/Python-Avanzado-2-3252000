def funcion_decorador(funcion):

    def funcion_wrapper():

        print("Dentro de la función wrapper")
        funcion()

    return funcion_wrapper


def funcion_prueba():
    print("Función de prueba")


# Añadir el decorador como instancia
funcion_prueba = funcion_decorador(funcion_prueba)
funcion_prueba()


# Añadir el decorador de manera Pythonica
@funcion_decorador
def funcion_prueba():
    print("Función de prueba")


funcion_prueba()
