class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento_identidad = None

    def agregar_documento_identidad(self, numero_documento):
        self.documento_identidad = numero_documento
        print("Documento guardado")

    def ejecutar_accion(self):
        print("Haciendo algo")


class Deportista(Persona):

    def __init__(self, nombre, apellido, edad, deporte):
        super().__init__(nombre, apellido, edad)
        self.deporte = deporte

    def ejecutar_accion(self):
        super().ejecutar_accion()
        print(f"Practicando {self.deporte}")


juliana = Deportista("Juliana", "Cortés", 26, "Volleyball")
juliana.agregar_documento_identidad(12345)
print(juliana.deporte)
juliana.ejecutar_accion()
