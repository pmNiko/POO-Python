import unittest
from operaciones_matematica import Resta


class TestResta(unittest.TestCase):
    def test_restaDeDosNumeros(self):
        resta = Resta()

        resta.operar(4, 2)

        self.assertEqual(resta.resultado, 2)

    def test_restablecerLaResta(self):
        resta = Resta()
        resta.operar(4, 2)

        self.assertEqual(resta.resultado, 2)

        resta.restablecer()

        self.assertEqual(resta.resultado, 0)


if __name__ == '__main__':
    unittest.main()
