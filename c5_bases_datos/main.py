from modelos import Departamento, Empleado
from conexion import engine, ModeloBase, session


def guardar_datos():
    contabilidad = Departamento("Contabilidad")
    session.add(contabilidad)
    tecnologia = Departamento("Tecnologia")
    session.add(tecnologia)
    session.commit()

    emilio = Empleado("Emilio", "Tafur", "1234", contabilidad.id)
    session.add(emilio)
    javier = Empleado("Javier", "Quiñonez", "567", tecnologia.id)
    session.add(javier)
    session.commit()


def hacer_consultas():
    departamento_1 = session.get(Departamento, 1)
    print(departamento_1)

    cantidad_departamentos = session.query(Departamento).count()
    print(cantidad_departamentos)

    empleados_contabilidad = session.query(Empleado).filter_by(id_departamento=departamento_1.id).all()
    print(empleados_contabilidad)

    for empleado in empleados_contabilidad:
        print(empleado)

    primer_empleados_contabilidad = session.query(Empleado).filter_by(nombre="Javier").first()
    print(primer_empleados_contabilidad)


if __name__ == "__main__":
    ModeloBase.metadata.create_all(engine)
    # guardar_datos()
    hacer_consultas()
