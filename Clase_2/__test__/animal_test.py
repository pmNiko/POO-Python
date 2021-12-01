import unittest
from animal import Animal


class TestAnimal(unittest.TestCase):
    def test_datosDeUnAnimal(self):
        """ Test un animal puede mostrar sus datos """
        gato = Animal("gato", 4, "miau")

        self.assertEqual(
            gato.datos(), 'Soy gato tengo 4 patas y hago miau.')


if __name__ == '__main__':
    unittest.main()