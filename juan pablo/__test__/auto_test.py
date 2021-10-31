import unittest
from auto import Auto

class TestAuto(unittest.TestCase):

    def setUp(self) -> None:
        self.auto = Auto()
    
    def test_detenerElAuto(self):
        """ El auto puede detenerce, no recibe parametros """
        self.auto.acelerar(100)

        self.assertEqual(self.auto.velocidad, 100)

        self.auto.detenerse()

        self.assertEqual(self.auto.velocidad, 0)

    def test_elAutoEstaParado(self):
        """ El auto esta en movimiento cuando su velocidad es 0 """

        self.assertFalse(self.auto.estaEnMovimiento())

    def test_elAutoNoPuedeTenerVelocidadNegativa(self):
        """ El auto no puede tener velocidad negativa """

        self.assertEqual(self.auto.velocidad, 0)

        with self.assertRaisesRegex(ValueError, 'La velocidad no puede ser negativa'):
            self.auto.acelerar(-100)

        self.assertEqual(self.auto.velocidad, 0)

    def test_acelerarLaVelocidadSeSuma(self):
        """ La velocidad de aceleracion se suma a la velocidad actual """
        self.auto.acelerar(100)

        self.assertEqual(self.auto.velocidad, 100)

        self.auto.acelerar(100)

        self.assertEqual(self.auto.velocidad, 200)


if __name__ == '__main__':
    unittest.main()
