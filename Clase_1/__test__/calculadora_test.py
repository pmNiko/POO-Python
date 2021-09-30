import unittest
from Clase_1.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    #  ----------- Test Suma -------------- #

    def test_SumarConLaCalculadora(self):
        """ Luego de ejecutar el metodo sumar 
            se valida el resultado de la calculadora. """
        calculadora = Calculadora()

        self.assertEqual(calculadora.resultado, 0)

        calculadora.sumar(2, 2)

        self.assertEqual(calculadora.resultado, 4)

        #  ----------- Test Resta -------------- #

    def test_RestarConLaCalculadora(self):
        """ Luego de ejecutar el metodo restar 
            se valida el resultado de la calculadora. """
        calculadora = Calculadora()

        self.assertEqual(calculadora.resultado, 0)

        calculadora.restar(5, 2)

        self.assertEqual(calculadora.resultado, 3)

        #  ----------- Test Division -------------- #

    def test_DivisionConLaCalculadora(self):
        """ Luego de ejecutar el metodo division 
            se valida el resultado de la calculadora. """
        calculadora = Calculadora()

        self.assertEqual(calculadora.resultado, 0)

        calculadora.dividir(12, 2)

        self.assertEqual(calculadora.resultado, 6)

        #  ----------- Test multiplicacion -------------- #

    def test_MultiplicarConLaCalculadora(self):
        """ Luego de ejecutar el metodo multiplicar 
            se valida el resultado de la calculadora. """
        calculadora = Calculadora()

        self.assertEqual(calculadora.resultado, 0)

        calculadora.multiplicar(5, 5)

        self.assertEqual(calculadora.resultado, 25)

        #  ----------- Test Borrar -------------- #

    def test_BorrarLaCalculadora(self):
        """ Luego de ejecutar el metodo borrar 
            se resetea el valor de la calculadora. """
        calculadora = Calculadora()
        calculadora.multiplicar(5, 5)

        self.assertEqual(calculadora.resultado, 25)

        calculadora.borrar()

        self.assertEqual(calculadora.resultado, 0)


if __name__ == "__main__":
    unittest.main()
