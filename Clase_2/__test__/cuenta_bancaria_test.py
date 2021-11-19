import unittest
from unittest.mock import patch
from cuenta_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    
    @patch.multiple(CuentaBancaria, __abstractmethods__=set())
    def test_depositarUnMontoEnUnaCuentaVacia(self):
        """ Test del metodo concreto depositar de la superclase """
        cuenta = CuentaBancaria('Carlos', 0)
        
        self.assertEqual(cuenta.saldo, 0)
        
        cuenta.depositar(100)
        
        self.assertEqual(cuenta.saldo, 100)

    @patch.multiple(CuentaBancaria, __abstractmethods__=set())
    def test_depositarUnMontoEnUnaCuentaConSaldo(self):
        """ Test del metodo concreto depositar de la superclase """
        cuenta = CuentaBancaria('Carlos', 100)
        
        self.assertEqual(cuenta.saldo, 100)
        
        cuenta.depositar(100)
        
        self.assertEqual(cuenta.saldo, 200)