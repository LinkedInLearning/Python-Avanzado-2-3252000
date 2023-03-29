class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.distancia_recorrida = 0

    def __add__(self, distancia):
        self.distancia_recorrida += distancia
        return self.distancia_recorrida

    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad


paco = Persona("Paco", 27)
emilio = Persona("Emilio", 26)

paco + 5
paco + 15
print(paco.distancia_recorrida)

print(paco < emilio)
print(emilio < paco)
