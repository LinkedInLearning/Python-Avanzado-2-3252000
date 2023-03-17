import time


def medir_tiempo_ejecucion(funcion):

    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejecución: {tiempo_total}")

    return wrapper


def decorador_puntos(funcion):

    def wrapper(*args, **kwargs):
        print("..........")
        funcion(*args, **kwargs)
        print("..........")

    return wrapper


@medir_tiempo_ejecucion
@decorador_puntos
def recorrer_ciclo(rango):

    for i in range(rango):
        print(i)
        time.sleep(1)


recorrer_ciclo(rango=5)
