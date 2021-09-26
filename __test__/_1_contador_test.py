import unittest
from Clase_1._1_contador import Contador


class Test_Contador1(unittest.TestCase):
    def test_incrementarElValor(self):
        """ Validamos el metodo incrementar el contador """
        contador = Contador()  # Setup

        # Precondición el contador esta en 0
        self.assertEqual(contador.valor, 0)

        contador.incrementar()  # Ejercitación del comportamiento

        self.assertEqual(contador.valor, 1)  # Objetivo del test

    def test_decrementarElValor(self):
        """ Validamos el metodo incrementar el contador """
        contador = Contador()  # Setup
        contador.incrementar()  # Setup

        # Precondición el contador esta en 1
        self.assertEqual(contador.valor, 1)

        contador.decrementar()  # Ejercitación del comportamiento

        self.assertEqual(contador.valor, 0)  # Objetivo del test

    def test_noSePuedeDecrementarCuandoEstaEnCero(self):
        """ Validamos el metodo incrementar el contador """
        contador = Contador()  # Setup

        # Precondición el contador esta en 0
        self.assertEqual(contador.valor, 0)

        self.assertRaises(ValueError, contador.decrementar)


if __name__ == "__main__":
    unittest.main()
