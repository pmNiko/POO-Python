import unittest
from operaciones_matematica import Division


class TestDivision(unittest.TestCase):
    def setUp(self) -> None:
        self.division = Division()

    def test_divisionDeDosNmeros(self):
        self.division.operar(8, 4)

        self.assertEqual(self.division.resultado, 2)

    def test_noSePuedeDividirPorCero(self):
        with self.assertRaisesRegex(ZeroDivisionError, 'No se puede divdir por 0.'):
            self.division.operar(8, 0)

    def test_restablecerLaDivision(self):
        division = Division()
        division.operar(4, 4)

        self.assertEqual(division.resultado, 1)

        division.restablecer()

        self.assertEqual(division.resultado, 0)


if __name__ == '__main__':
    unittest.main()
