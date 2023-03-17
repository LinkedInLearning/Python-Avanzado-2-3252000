import time


def medir_tiempo_ejecucion(funcion):

    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejecución: {tiempo_total}")

    return wrapper


@medir_tiempo_ejecucion
def recorrer_ciclo():

    for i in range(5):
        print(i)
        time.sleep(1)


recorrer_ciclo()
