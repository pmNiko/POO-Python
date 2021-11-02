import unittest
from puente import Puente

class TestPuente(unittest.TestCase):
    def setUp(self) -> None:
        self.puente = Puente(1)
        

    def test_verSiLaVallaEstaAlta(self):
        """ Un puente puede saber si su valla esta alta """
        self.assertTrue(self.puente.laVallaEstaAlta())

    def test_puentePuedeBajarLaValla(self):
        """ Puede bajar la valla """
        self.assertTrue(self.puente.laVallaEstaAlta())

        self.puente.bajarLaValla()

        self.assertFalse(self.puente.laVallaEstaAlta())

    def test_puentePuedeSubirLaValla(self):
        """ Puede subir la valla """
        self.puente.bajarLaValla()

        self.assertFalse(self.puente.laVallaEstaAlta())

        self.puente.subirLaValla() 

        self.assertTrue(self.puente.laVallaEstaAlta())

    
        

        


        