import asyncio
import time


def funcion_sincrona():
    print("Ejecutando función síncrona")
    time.sleep(1)
    print("Fin función síncrona")


async def funcion_asincrona():
    print("Ejecutando función asíncrona")
    await asyncio.sleep(1)
    print("Fin función asíncrona")


async def main():
    corrutinas = [funcion_asincrona(), funcion_asincrona()]
    await asyncio.gather(*corrutinas)

inicio = time.time()
asyncio.run(main())
print(f"Tiempo asíncrono: {time.time() - inicio}")

inicio = time.time()
funcion_sincrona()
funcion_sincrona()
print(f"Tiempo síncrono: {time.time() - inicio}")
