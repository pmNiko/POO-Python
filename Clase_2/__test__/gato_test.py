import unittest
from gato import Gato


class TestGato(unittest.TestCase):
    def test_datosDeUnGato(self):
        """ Test hereda el metodo datos de la superclase """
        gato = Gato("gato", 4, "miau")

        self.assertEqual(
            gato.datos(), 'Soy gato tengo 4 patas y hago miau.')


if __name__ == '__main__':
    unittest.main()
