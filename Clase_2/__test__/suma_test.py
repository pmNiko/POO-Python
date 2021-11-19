import unittest
from operaciones_matematica import Suma


class TestSuma(unittest.TestCase):
    def test_sumaDeDosNumeros(self):
        suma = Suma()

        self.assertEqual(suma.resultado, 0)

        suma.operar(2, 2)

        self.assertEqual(suma.resultado, 4)

    def test_restablecerLaSuma(self):
        suma = Suma()
        suma.operar(2, 2)

        self.assertEqual(suma.resultado, 4)

        suma.restablecer()

        self.assertEqual(suma.resultado, 0)


if __name__ == '__main__':
    unittest.main()
