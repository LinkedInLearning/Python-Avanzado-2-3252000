import unittest


def calcular_promedio_try_except(lista):
    try:
        promedio = sum(lista) / len(lista)
        return promedio
    except Exception as e:
        return None


def calcular_promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio


class Test(unittest.TestCase):

    def test_promedio_exitoso_try_except(self):
        lista = [2, 3, 4]
        promedio_esperado = 3
        promedio_obtenido = calcular_promedio_try_except(lista)
        self.assertEqual(promedio_esperado, promedio_obtenido)

    def test_promedio_none_try_except(self):
        lista_vacia = []
        promedio_obtenido = calcular_promedio_try_except(lista_vacia)
        self.assertIsNone(promedio_obtenido)

    def test_promedio_exitoso(self):
        lista = [2, 3, 4]
        promedio_esperado = 3
        promedio_obtenido = calcular_promedio(lista)
        self.assertEqual(promedio_esperado, promedio_obtenido)

    def test_promedio_falla(self):
        with self.assertRaises(Exception):
            lista_vacia = []
            calcular_promedio(lista_vacia)


if __name__ == '__main__':
    unittest.main()
