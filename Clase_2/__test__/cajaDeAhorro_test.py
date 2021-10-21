import unittest
from cajaDeAhorro import CajaDeAhorro
from excepciones import ImposibleRealizarExtraccion


class TestCajaDeAhorro(unittest.TestCase):
    # ------ setup de la clase CajaDeAhorro ------ #
    def setUp(self) -> None:
        self.cuenta = CajaDeAhorro('Ruben', 0, 2)

    
    def test_cuentaInicializaConElMontoEspecificado(self):
        """ Al crear la caja de ahorro se especifica el saldo inicial """
        cuenta = CajaDeAhorro('Marcos', 100, 2)

        self.assertEqual(cuenta.saldo, 100)

    
    def test_depositarSaldoEnUnaCuenta(self):
        """ Se deposita un monto en una caja de ahorro """
        self.assertEqual(self.cuenta.saldo, 0)

        self.cuenta.depositar(100)
        self.cuenta.depositar(1000)

        self.assertEqual(self.cuenta.saldo, 1100)
        
    
    def test_NoSePuedeExtreaerUnMonto(self):
        """ El monto de la extracción supera el saldo """
        self.assertFalse(self.cuenta.puedeExtraer(100))
        
        
    def test_sePuedeExtreaerUnMonto(self):
        """ El monto de la extracción es menor o igual al saldo """
        self.cuenta.depositar(150)
        
        self.assertTrue(self.cuenta.puedeExtraer(100))
  

    def test_extraerDineroDeUnaCuenta(self):
        """ Extracción de una caja de ahorro """
        self.cuenta.depositar(1000)

        self.assertEqual(self.cuenta.saldo, 1000)

        self.cuenta.extraer(500)

        self.assertEqual(self.cuenta.saldo, 500)

   
    def test_extraerDineroDeUnaCuentaVacia(self):
        """ Se intenta realizar una extracción superior al saldo """
        self.assertEqual(self.cuenta.saldo, 0)

        with self.assertRaisesRegex(ImposibleRealizarExtraccion, "Imposible realizar la extracción."):
            self.cuenta.extraer(500)

        self.assertEqual(self.cuenta.saldo, 0)
        
    def test_cantidadDeExtraccionesValidas(self):
        """ La caja fue creada con un maximo de dos extracciones maximas """
        self.cuenta.depositar(1000)
        
        self.assertEqual(self.cuenta.extraccionesPosibles, 2)
        self.assertEqual(self.cuenta.extraccionesRealizadas, 0)
        
        self.cuenta.extraer(100)
        self.cuenta.extraer(100)

        self.assertEqual(self.cuenta.extraccionesRealizadas, 2)
        
        
    def test_cantidadDeExtraccionesNoValidas(self):
        """ La caja fue creada con un maximo de dos extracciones maximas """
        self.cuenta.depositar(1000)
        
        self.assertEqual(self.cuenta.extraccionesRealizadas, 0)
        
        self.cuenta.extraer(100)
        self.cuenta.extraer(100)
        
        with self.assertRaisesRegex(ImposibleRealizarExtraccion, "Imposible realizar la extracción."):
            self.cuenta.extraer(100)
        self.assertEqual(self.cuenta.extraccionesRealizadas, 2)
        
    
    def test_restaurarLasExtracciones(self):
        """ La caja de ahorro puede restaurar las extracciones a 0 """
        self.cuenta.depositar(1000)
        self.cuenta.extraer(100)
        self.cuenta.extraer(100)
        
        self.assertEqual(self.cuenta.extraccionesRealizadas, self.cuenta.extraccionesPosibles)
        
        self.cuenta.restaurarExtraciones()
        
        self.assertNotEqual(self.cuenta.extraccionesRealizadas, self.cuenta.extraccionesPosibles)
        self.assertEqual(self.cuenta.extraccionesRealizadas, 0)
        
        
if __name__ == "__main__":
    unittest.main()
