import unittest
from cuentaCorriente import CuentaCorriente
from excepciones import ImposibleRealizarExtraccion


class TestCuentaCorriente(unittest.TestCase):
    # ------ setup de la clase CuentaCorriente ------ #
    def setUp(self) -> None:
        self.cuenta = CuentaCorriente('Pedro', 0, 500)

    
    def test_cuentaInicializaConElMontoEspecificado(self):
        """ Al crear la caja de ahorro se especifica el saldo inicial """
        cuenta = CuentaCorriente('Marcos', 100, 200)

        self.assertEqual(cuenta.saldo, 100)
        
    def test_depositarSaldoEnUnaCuenta(self):
        """ Se deposita un monto en una cuenta corriente """
        self.assertEqual(self.cuenta.saldo, 0)
        
        self.cuenta.depositar(100)

        self.assertEqual(self.cuenta.saldo, 100)
        
    def test_depositarSaldoEnUnaCuentaConSaldo(self):
        """ Se deposita un monto en una cuenta corriente con saldo"""
        self.cuenta.depositar(100)
        
        self.assertEqual(self.cuenta.saldo, 100)
        
        self.cuenta.depositar(100)

        self.assertEqual(self.cuenta.saldo, 200)

    def test_sePuedeExtraerUnMontoEnDescubierto(self):
        """ Se puede extraer un monto en descubierto """        
        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.descubiertoMaximo, 500)
        
        self.assertTrue(self.cuenta.puedeExtraer(500))

    def test_montoEnDescubiertoNoAdmisible(self):
        """ No se puede extraer un monto en descubierto """        
        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.descubiertoMaximo, 500)
        
        self.assertFalse(self.cuenta.puedeExtraer(501))

    def test_extraccionEnDescubiertoDeUnaCuentaVacia(self):
        """ Se realiza una extracción en descubierto """        
        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.descubiertoMaximo, 500)
        
        self.cuenta.extraer(200)
        
        self.assertEqual(self.cuenta.saldo, -200)

    def test_seIntentaRealizarUnaExtraccionNoPermitida(self):
        """ Se realiza una extracción en descubierto """        
        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.descubiertoMaximo, 500)
        
        with self.assertRaisesRegex(ImposibleRealizarExtraccion, "Imposible realizar la extracción."):
          self.cuenta.extraer(501)
        
        self.assertEqual(self.cuenta.saldo, 0)
        


        
        
if __name__ == "__main__":
    unittest.main()
