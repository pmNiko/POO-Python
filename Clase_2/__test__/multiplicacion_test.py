import unittest
from operaciones_matematica import Multiplicacion


class TestMultiplicacion(unittest.TestCase):
    def test_multiplicacionDeDosNumeros(self):
        multiplicacion = Multiplicacion()

        multiplicacion.operar(4, 4)

        self.assertEqual(multiplicacion.resultado, 16)

    def test_restablecerLaMultiplicacion(self):
        multiplicacion = Multiplicacion()
        multiplicacion.operar(4, 4)

        self.assertEqual(multiplicacion.resultado, 16)

        multiplicacion.restablecer()

        self.assertEqual(multiplicacion.resultado, 0)


if __name__ == '__main__':
    unittest.main()
