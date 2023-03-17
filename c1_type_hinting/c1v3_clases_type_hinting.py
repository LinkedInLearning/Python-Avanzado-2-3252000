class Persona:

    def __init__(self, nombre: str, posicion: int) -> None:
        self.nombre = nombre
        self.posicion = posicion

    def caminar(self, distancia_km: int) -> int:
        self.posicion += distancia_km
        return self.posicion


paco = Persona(nombre="Paco", posicion=0)
posicion_paco = paco.caminar(distancia_km=6)
