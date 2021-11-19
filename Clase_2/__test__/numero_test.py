import unittest
from numero import Numero


class TestNumero(unittest.TestCase):
    def setUp(self) -> None:
        self.numero_1 = Numero(1)
        self.numero_5 = Numero(5)

    def test_unNumeroEsIgualAOtroNumero(self):
        """ El numero 1 es igual a otro numero 1 """
        numero_1 = Numero(1)

        self.assertTrue(self.numero_1 == numero_1)

    def test_unNumeroEsDistintoAOtroNumero(self):
        """ El numero 1 no es igual al numero 5 """

        self.assertFalse(self.numero_1 == self.numero_5)

    def test_unNumeroEsMenorAOtroNumero(self):
        """ El numero 1 es menor al numero 5 """

        self.assertTrue(self.numero_1 < self.numero_5)

    def test_unNumeroNoEsMenorAOtroNumero(self):
        """ El numero 5 no es menor al numero 1 """

        self.assertFalse(self.numero_5 < self.numero_1)

    def test_unNumeroEsMenorOIgualAOtroNumero(self):
        """ El numero 1 es menor o igual a 5 """

        self.assertTrue(self.numero_1 <= self.numero_5)

    def test_unNumeroEsMayorOIgualAOtroNumero(self):
        """ El numero 1 es mayor o igual a 5 """

        self.assertTrue(self.numero_5 >= self.numero_1)

    def test_unNumeroEsMayorAOtroNumero(self):
        """ El numero 5 es mayor a 1 """

        self.assertTrue(self.numero_5 > self.numero_1)

    def test_unNumeroNoEsMayorAOtroNumero(self):
        """ El numero 1 no es mayor a 5 """

        self.assertFalse(self.numero_1 > self.numero_5)

    def test_unNumeroEstaEntreDosNumeros(self):
        """ El numero 3 esta entre el 1 y el 5 """
        numero_3 = Numero(3)

        self.assertTrue(numero_3.entreDosNumeros(self.numero_1, self.numero_5))

    def test_unNumeroFueraDeRango(self):
        """ El numero 6 esta fuera del rango de 1 y 5"""
        numero_6 = Numero(6)

        self.assertFalse(numero_6.entreDosNumeros(self.numero_1, self.numero_5))


if __name__ == '__main__':
    unittest.main()
