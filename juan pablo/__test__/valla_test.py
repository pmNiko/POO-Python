import unittest
from valla import Valla

class TestValla(unittest.TestCase):
    def setUp(self) -> None:
        self.valla = Valla()
    
    def test_laVallaInicialmenteEstaAlta(self):
        """ cuando inicia la valla esta alta """
        self.assertTrue(self.valla.alta)

    def test_laVallaSePuedeBajar(self):
        """ Se puede bajar la valla """
        self.assertTrue(self.valla.alta)
        
        self.valla.cambiarEstado()

        self.assertFalse(self.valla.alta)

    def test_laVallaSePuedeLevantar(self):
        self.valla.cambiarEstado()

        self.assertFalse(self.valla.alta)

        self.valla.cambiarEstado()

        self.assertTrue(self.valla.alta)